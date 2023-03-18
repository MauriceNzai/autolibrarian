"""
Holds all the views for the autolibapp
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Renders the index page
    """
    return render(request,'index.html')
