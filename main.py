from fastapi.templating import Jinja2Templates 
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main_html(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})