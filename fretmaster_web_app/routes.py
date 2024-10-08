from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/")
def index(request: Request):
    return templates.TemplateResponse('shared/main.html', {"request": request,
                                                           "page_description":
                                                               "appears in the <head> "
                                                               "of the html"})
