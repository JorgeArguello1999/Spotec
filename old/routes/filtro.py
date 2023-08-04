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
@router.get('/filtro')
async def tabla_juego(request: Request, cedula: int= 0, idjugador: int= 0):

    equipos = vista.lista_equipos(cedula=0, idjugador=0)

    if cedula != 0:
        equipos = vista.lista_equipos(cedula, idjugador=0)

    if idjugador != 0 :
        equipos = vista.lista_equipos(cedula=0, idjugador=idjugador)

    if cedula != 0 and idjugador != 0:
        equipos = vista.lista_equipos(cedula, idjugador)


    return templates.TemplateResponse('filtro.html', {
        "request": request,
        "equipos": equipos
    })
