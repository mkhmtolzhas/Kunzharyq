from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from parser.music import get_content as get_content_music, get_html as get_music_html, URL


router = APIRouter(
    prefix="",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="template")

@router.get("/")
def get_main_page(request : Request):
    html = get_music_html(url=URL)
    musics = get_content_music(html.text)
    response = {
        "request" : request,
        "musics" : musics
    }
    return templates.TemplateResponse("index.html", response)