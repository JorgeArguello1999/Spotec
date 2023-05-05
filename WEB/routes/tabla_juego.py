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
async def tabla_juego(request: Request, idevento: int = None, idgenero: int = None, idestilo: int = None):

    lista = vista.lista_categorias()
    genero = vista.lista_genero()
    estilos = vista.lista_estilos()

    if idevento == None:
        data = vista.tabla_juego()
        print("Todas las tablas")
    if idgenero != None or idestilo != None:
        data = vista.tabla_juego_genero_estilo(idgenero, idestilo)
    if idevento != None:
        data = vista.tabla_juego_categoria(idevento)
        print("Usando el buscador")

    # vista.get_carriles(data)

    return templates.TemplateResponse('tabla_juego.html', {
        "request": request,
        "data": data,
        "lista": lista,
        "genero": genero,
        "estilos": estilos
    })
