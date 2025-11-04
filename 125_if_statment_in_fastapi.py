from fastapi import FastAPI

app = FastAPI()

@app.post('/{id}')
def fuond_blog(id:int):
    if id > 5:
        return 'blog not found'
    else:
        return f'the blog {id} is found'
