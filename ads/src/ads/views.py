from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.

def test (request):
    return render (request , 'index.html' , {})
