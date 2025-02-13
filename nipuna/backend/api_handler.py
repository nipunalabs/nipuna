import uvicorn
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from ..scripts.frontend_build import build_frontend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def mount_components():
    app.mount("/static/assets", StaticFiles(directory="../ui/dist/static/assets", html=True), name="assets")
    app.mount("/ui", StaticFiles(directory="../ui/dist"), name="ui")


@app.get("/rand")
async def hello():
    return(str(random.randint(0,100)))

@app.get('/')
async def client():  return FileResponse("../ui/dist/index.html")

def start_components():
    build_frontend()
    mount_components()
    uvicorn.run(app, host="0.0.0.0", port=8000)

