"""
URLS for the autolibapp are included here
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('addbook/', views.addbook, name='addbook'),
        path('deletebook/<int:id>', views.deletebook, name='deletebook'),
        path('bookissue/', views.bookissue, name='bookissue'),
        path('returnbook/', views.returnbook, name='returnbook'),
        path('editbookdetails/<int:id>', views.editbookdetails, name='editbookdetails'),
        path('<int:id>/updatedetails/', views.updatedetails, name='updatedetails'),
        path('addmember/' ,views.addstudent, name='addmember'),
    ]
