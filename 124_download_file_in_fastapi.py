from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
app = FastAPI()
app.mount('/projects', StaticFiles(directory='projects'), name='projects')

@app.post('/donload/{name}', response_class=FileResponse)
def donload(name:str):
    path = f'CODEING/projects/{name}'
    return path
