"""
Holds all the views for the autolibapp
"""
from datetime import datetime, timedelta, date
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as dj_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.shortcuts import render, HttpResponse,redirect
from .models import Book, IssueBook, LibUser, Member, ReturnBook

# Create your views here.
def index(request):
    """
    Renders the index page
    """
    return render(request,'index.html')

def dashboard(request):
    """
    Redirects to the user's dashboard
    """
    if request.session.has_key('is_logged'):
        Book = Book.objects.all()
        return render(request,'dashboard.html',{'Book':Book})
    return redirect('stafflogin')


def addbook(request):
    """
    Rdirects to the addbook page
    """
    Book = Book.objects.all()
    return render(request,'addbook.html',{'Book':Book})

def deletebook(request, id):
    """
    Redirects to the delete book page if user is logged in
    or redirect to login page if user not logged in
    """
    if request.session.has_key('is_logged'):
        AddBook_info = Book.objects.get(id=id)
        AddBook_info.delete()
        return redirect("dashboard")
    return redirect("login")


def bookissue(request):
    """
    Redirescts to the book issue page
    """
    return render(request,'bookissue.html')


def returnbook(request):
    """
    Redirects to the return book page
    """
    return render(request,'returnbook.html')

def editbookdetails(request,id):
    """
    Redirects to the edit book dteails page or 
    login page if user not already logged in
    """
    if request.session.has_key('is_logged'):
        Book = Book.objects.get(id=id)
        return render(request,'editdetails.html',{'Book':Book})
    return redirect('login')


def updatedetails(request,id):
    """
    """
    if request.session.has_key('is_logged'):

        if request.method == "POST":
            add = Book.objects.get(id = id)
            add.bookid = request.POST["bookid"]
            add.bookname = request.POST["bookname"]
            add.subject = request.POST["subject"]
            add.ContactNumber = request.POST['category']
            add.save()
            return redirect("dashboard")
    return redirect('login')


def addstudent(request):
    """
    Ridrects to add sutdent page if user is logged in
    or login page if user not already logged in
    """
    if request.session.has_key('is_logged'):
       return render(request,'addstudent.html')
    return redirect ('login')
