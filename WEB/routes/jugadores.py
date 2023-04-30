from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import jinja2

from Conectors.views import vistas

router = APIRouter()
vista = vistas()

# Configuramos el Conector
templates = Jinja2Templates(directory="templates")

@router.get('/jugadores')
async def tabla_juego(request: Request, provincia: str = None, cedula: str = None):
    
    provincias = vista.lista_provincias()
    out = vista.listar_jugadores()

    if provincia != None or cedula != None:
        out = vista.listar_jugadores_fill(provincia, cedula)



    return templates.TemplateResponse('jugadores.html', {
        "request": request,
        "data": out,
        "provincias": provincias
    })
