from fastapi import FastAPI,status,Response
from enum import Enum




app = FastAPI()
    

@app.get("/blog/{id}", status_code=status.HTTP_200_OK)
def get_blogs(id: int, response:Response):

    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"ERROR" : f"Blog {id} NOT FOUND!!!"}

    return {"massege" : f"Blog {id}"} 