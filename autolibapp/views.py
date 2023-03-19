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
    return render(request, 'index.html')

def staff(request):
    """
    Redirects to the staff page for user to either signup or login
    """
    return render(request, 'staff.html')

def staffsignup(request):
    """
    Redirects to the signup page
    """
    return render(request, 'staffsignup.html')

def signupbackend(request):
    """
    Performs the  staff signup backend processes
    """
    if request.method =='POST':
        uname = request.POST["uname"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        phone = request.POST['phone']
        password = request.POST['password']
        userprofile = LibUser(phone = phone)
        if request.method == 'POST':
            try:
                UserExists = User.objects.get(username = request.POST['uname'])
                messages.error(request, " Username already taken, Try something else!!!")
                return redirect("staffsignup")
            except User.DoesNotExist:
                if len(uname)>10:
                    messages.error(request," Username must be max 10 characters, Please try again")
                    return redirect("staffsignup")

                if not uname.isalnum():
                    messages.error(request,
                            " Username should only contain letters and numbers, Please try again")
                    return redirect("staffsignup")

        # create the user
        user = User.objects.create_user(uname, email, password)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        userprofile.user = user
        userprofile.save()
        messages.success(request," Your account has been successfully created")
        return redirect("stafflogin")
    else:
        return HttpResponse('404 - NOT FOUND ')

def stafflogin(request):
    """
    Redirects to the staff login page
    """
    if request.session.has_key('is_logged'):
        return redirect('dashboard')
    return render(request,'stafflogin.html')

def loginbackend(request):
    """
    Handles the login backend processes
    """
    if request.method =='POST':
        loginuname = request.POST["loginuname"]
        loginpassword=request.POST["loginpassword"]
        registereduser = authenticate(username=loginuname, password=loginpassword)
        if registereduser is not None:
            dj_login(request, registereduser)
            request.session['is_logged'] = True
            registereduser = request.user.id
            request.session["user_id"] = registereduser
            messages.success(request, " Successfully logged in")
            return redirect('dashboard')
        else:
            messages.error(request," Invalid Credentials, Please try again")
            return redirect("/")
    return HttpResponse('404-not found')

def stafflogout(request):
    """
    Logs user out of the session
    """
    del request.session['is_logged']
    del request.session["user_id"]
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('dashboard')

def dashboard(request):
    """
    Redirects to the user's dashboard
    """
    if request.session.has_key('is_logged'):
        book = Book.objects.all()
        return render(request,'dashboard.html',{'Book':book})
    return redirect('stafflogin')


def addbook(request):
    """
    Rdirects to the addbook page
    """
    book = Book.objects.all()
    return render(request,'addbook.html',{'Book':book})

def addbookbackend(request):
    """
    Handles the backend processes of book addition
    """
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id = user_id)
            bookid = request.POST["bookid"]
            isbn = request.POST["isbn"]
            author = request.POST["author"]
            booktitle = request.POST["booktitle"]
            subject = request.POST["subject"]
            category=request.POST["category"]
            add = Book(user = user1, bookid = bookid, isbn = isbn, booktitle = booktitle,
                    author = author, subject = subject, category = category)
            add.save()
            book = Book.objects.all()
            return render(request, 'dashboard.html', {'Book':book})
    return redirect('/')

def editbookdetails(request, id):
    """
    Redirects to the edit book details page
    """
    if request.session.has_key('is_logged'):
        Book = Book.objects.get(id=id)
        return render(request, 'editdetails.html', {'Book':Book})
    return redirect('login')

def updatedetails(request,id):
    """
    Handles the backend processes of editing book details
    """
    if request.session.has_key('is_logged'):

        if request.method=="POST":
            add = Book.objects.get(id = id)
            add.bookid = request.POST["bookid"]
            add.isbn = request.POST["isbn"]
            add.booktitle = request.POST["booktitle"]
            add.author = request.POST["author"]
            add.subject = request.POST["subject"]
            add.category = request.POST['category']
            add.save()
            return redirect("dashboard")
    return redirect('login')

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

def issuebookbackend(request):
    """
    Handles issue book backend processes
    """
    if request.method=='POST':
        user_id = request.session["user_id"]
        user1 = User.objects.get(id=user_id)
        memberid = request.POST['memberid']
        book1 = request.POST['book1']
        store = Book.objects.filter(bookid = book1)

def get_category(addbook):
    """
    Helper function for book issue functionality
    """
    if addbook.category == "Not-Issued":
        addbook.category = "Issued"
        obj = IssueBook(user = user1, memberid = memberid, book1 = book1)
        obj.save()
        addbook.save()
    else:
        messages.error(request," Book already issued !!!")
        category_list = list(set(map(get_category,store)))
        Issue=IssueBook.objects.all()
        return render(request, 'bookissue.html', {'Issue':Issue})
    return redirect('/')

def returnbook(request):
    """
    Redirects to the return book page
    """
    return render(request,'returnbook.html')

def returnbookbackend(request):
    """
    Handles backend processes of returning a book
    """
    if request.method=='POST':
        user_id = request.session["user_id"]
        user1 = User.objects.get(id = user_id)
        bookid2 = request.POST['bookid2']
        store1 = Book.objects.filter(bookid = bookid2)

def return_book(returnbook):
    """
    Helper function for return book functionality
    """
    if returnbook.category == "Issued":
        returnbook.category = "Not-Issued"
        obj1=ReturnBook(user = user1, bookid2 = bookid2)
        obj=IssueBook.objects.filter(book1 = bookid2)
        obj.delete()
        obj1.save()
        return book.save()
    else:
        messages.error(request," Book not  issued !!!")
        returncategorylist = list(set(map(return_book, store1)))
        Return = ReturnBook.objects.all()
        return render(request, 'returnbook.html', {'Return':Return})
    return redirect('/')

def editbookdetails(request, id):
    """
    Redirects to the edit book dteails page or 
    login page if user not already logged in
    """
    if request.session.has_key('is_logged'):
        AddBook=Book.objects.get(id = id)
        return render(request,'editdetails.html',{'Book':Book})
    return redirect('login')

def updatedetails(request, id):
    """
    Updates details of a given book
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


def addmember(request):
    """
    Ridrects to add sutdent page if user is logged in
    or login page if user not already logged in
    """
    if request.session.has_key('is_logged'):
       return render(request, 'addstudent.html')
    return redirect ('login')
