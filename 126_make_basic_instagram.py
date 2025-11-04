from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from typing import List
import os
import bcrypt


app = FastAPI()



users = {}
posts = []



class User(BaseModel):
    username: str
    password: str


class Post(BaseModel):
    id: int
    user_id: int
    caption: str
    image_url: str


class Comment(BaseModel):
    id: int
    post_id: int
    user_id: int
    text: str


async def authenticate_user(username: str, password: str):
    if username in users:
        hashed_password = users[username]["password"]
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")):
            return users[username]
    return None



async def get_current_user(username: str, password: str):
    return await authenticate_user(username, password)



@app.post("/signup")
async def signup(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Username already taken")
    user_id = len(users) + 1
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    users[user.username] = {"password": hashed_password, "posts": [], "id": user_id}
    return JSONResponse(content={"message": "User created successfully", "user_id": user_id, "hashed_password": hashed_password}, status_code=201)



@app.post("/login")
async def login(user: User):
    authenticated_user = await authenticate_user(user.username, user.password)
    if authenticated_user:
        return JSONResponse(content={"message": "Logged in successfully"}, status_code=200)
    raise HTTPException(status_code=401, detail="Invalid credentials")



@app.post("/logout")
async def logout(username: str, password: str):
    authenticated_user = await authenticate_user(username, password)
    if authenticated_user:
        del users[username]
        return JSONResponse(content={"message": "Logged out successfully"}, status_code=200)
    raise HTTPException(status_code=401, detail="Invalid credentials")



async def save_file(file: UploadFile):
    


    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return file_path



@app.post("/post")
async def create_post(username: str, password: str, caption: str, image: UploadFile = File(...)):
    authenticated_user = await authenticate_user(username, password)
    if authenticated_user:
        post_id = len(posts) + 1
        posts.append({"id": post_id, "user_id": username, "caption": caption, "image_url": await save_file(image)})
        users[username]["posts"].append(post_id)
        return JSONResponse(content={"message": "Post created successfully", "post_id": post_id}, status_code=201)
    raise HTTPException(status_code=401, detail="Invalid credentials")



@app.post("/comment/{post_id}")
async def create_comment(post_id: int, username: str, password: str, text: str):
    authenticated_user = await authenticate_user(username, password)
    if authenticated_user:
        post = next((post for post in posts if post["id"] == post_id), None)
        if post:
            comment_id = len([comment for post in posts for comment in post.get("comments", [])]) + 1
            post.setdefault("comments", []).append({"id": comment_id, "user_id": username, "text": text})
            return JSONResponse(content={"message": "Comment created successfully"}, status_code=201)
        raise HTTPException(status_code=404, detail="Post not found")
    raise HTTPException(status_code=401, detail="Invalid credentials")



@app.get("/posts")
async def get_all_posts():
    return JSONResponse(content={"posts": posts}, status_code=200)



@app.delete("/post/{post_id}")
async def delete_post(post_id: int, user: User = Depends(get_current_user)):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post and post["user_id"] == user.username:
        posts.remove(post)
        users[user.username]["posts"].remove(post_id)
        return JSONResponse(content={"message": "Post deleted successfully"}, status_code=200)
    raise HTTPException(status_code=404, detail="Post not found or unauthorized")