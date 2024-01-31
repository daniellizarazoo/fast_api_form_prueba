from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def main_html(
    request: Request, 
    fname: str | None = None, 
    city: str | None = None,
    eaddress: str | None = None,
    phone: str | None = None
):
    return templates.TemplateResponse("/index.html", {"request": request})

if __name__ == "__main__":
    # Run the app using uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
