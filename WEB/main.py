from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2
import uvicorn
import os

# Configuramos las routas de los diferentes modulos
from routes.tabla_juego import router as tabla_juego
from routes.jugadores import router as jugadores

# Configuramos FastAPi
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rutas en modulos externos
app.include_router(tabla_juego)
app.include_router(jugadores)


if __name__ == '__main__':
    db_url = os.getenv('DB_URL')
    uvicorn.run(app, host=db_url, port=8000)
