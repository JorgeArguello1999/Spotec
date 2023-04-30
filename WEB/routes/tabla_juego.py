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
@router.get('/tabla_juego')
async def tabla_juego(request: Request, idevento: int = None):

    lista = vista.tabla_juego()

    if idevento == None:
        out = vista.lista_categorias()
        data = vista.tabla_juego()
        print("Todas las tablas")
    else:
        out = vista.lista_categorias_fill(idevento)
        data = vista.tabla_juego_categoria(idevento)
        print("Usando el buscador")

    return templates.TemplateResponse('tabla_juego.html', {
        "request": request,
        "lista_categorias": out,
        "data": data,
        "lista": lista
    })
