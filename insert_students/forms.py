from django.forms import ModelForm
from .models import create_student

class create_student_form(ModelForm):
    class Meta:
        model = create_student
        fields = ["nombre", "cedula", "provincia", "escuela"]