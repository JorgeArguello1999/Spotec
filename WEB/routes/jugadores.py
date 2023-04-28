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

@router.route('/jugadores', methods=['GET', 'POST'])
async def tabla_juego(request: Request):
    lista_jugadores = vista.listar_jugadores()
    data = vista.tabla_juego()

    '''
    form = await request.form()
    try:
        lista_categorias= vista.lista_categorias_fill(form['select'])
        print("Usando el buscador")
    except:
        print("Todas las tablas")
    '''
    
    return templates.TemplateResponse('jugadores.html', {
        "request": request,
        "data": lista_jugadores,
    })
