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

# @router.route('/tabla_juego', methods=['GET', 'POST'])
@router.get('/equipos')
async def tabla_juego(request: Request, equipo: str = None, provincia: str = None):

    provincias = vista.lista_provincias()
    equipos = vista.lista_equipos()

    return templates.TemplateResponse('equipos.html', {
        "request": request,
        "equipos": equipos,
        "provincias": provincias
    })
