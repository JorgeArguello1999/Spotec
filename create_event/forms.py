from django.forms import ModelForm
from .models import create_evento

class create_evento_form(ModelForm):
    class Meta:
        model = create_evento
        fields = ["nombre"]