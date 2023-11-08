from django.contrib import admin
from .models import *

# Register your models here.
Models = [
    EspaldaHombre, LibreHombre, BrazaHombre, MariposaHombre,
    EspaldaMujer, LibreMujer, BrazaMujer, MariposaMujer
]

admin.site.register(Models)