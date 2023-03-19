"""
URLS for the autolibapp are included here
"""

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name = 'index'),
        path('dashboard/', views.dashboard, name = 'dashboard'),
        path('addbook/', views.addbook, name = 'addbook'),
        path('addbookbackend/', views.addbookbackend, name = 'addbookbackend'),
        path('deletebook/<int:id>', views.deletebook, name = 'deletebook'),
        path('bookissue/', views.bookissue, name = 'bookissue'),
        path('returnbook/', views.returnbook, name = 'returnbook'),
        path('editbookdetails/<int:id>', views.editbookdetails, name = 'editbookdetails'),
        path('<int:id>/updatedetails/', views.updatedetails, name = 'updatedetails'),
        path('addmember/', views.addmember, name = 'addmember'),
        path('staff/', views.staff, name = 'staff'),
        path('staffsignup/', views.staffsignup, name = 'staffsignup'),
        path('signupbackend/', views.signupbackend, name = 'signupbackend'),
        path('stafflogin/', views.stafflogin, name = 'stafflogin'),
        path('loginbackend/', views.loginbackend, name = 'loginbackend'),
        path('stafflogout/', views.stafflogout, name = 'stafflogout'),
    ]
