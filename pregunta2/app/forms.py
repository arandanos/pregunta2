from django import forms

from .models import Test, Pregunta

class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test 
        fields = ('tema',)

class PreguntaForm(forms.ModelForm):
    
    class Meta:
        model = Pregunta
        fields = ('texto',)
