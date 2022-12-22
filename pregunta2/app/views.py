from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TestForm

# Create your views here.
@csrf_exempt
def index(request):
  return render(request, 'index.html')

@csrf_exempt
def test(request):
  formTest= TestForm()
  context = {
    'form_test': formTest
  }
  return render(request, 'test_edit.html', context)

