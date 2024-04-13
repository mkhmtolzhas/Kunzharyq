from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router.pages.pages import router as pages_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(pages_router)