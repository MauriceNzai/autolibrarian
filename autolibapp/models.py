"""
Has all the models representing the database tables
"""
from datetime import datetime,timedelta
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


class LibUser(models.Model):
    """
    models the user, extending the inbuilt User model
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):

        """
        Return readable string representing the LibUser model
        """
        return self.user.username


class Book(models.Model):
    """
    Models a book to store all book information
    """
    user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    book_id = CharField(max_length=10)
    book_title = CharField(max_length=50)
    isbn = models.CharField('ISBN', max_length=25)
    subject = CharField(max_length=20)
    category= models.CharField(max_length = 10)
    book_author = models.CharField(max_length = 50, null=True)

    def __str__(self):
        """
        Returns readable string
        """
        return str(self.book_title)+"["+str(self.book_id)+']'


class Member(models.Model):
    """
    Models the library member to store information of a borrower
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    member_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        """
        Return readable string representing the Member model
        """
        return self.first_name + self.last_name + '['+str(self.member_id)+']'


def expiry():
    """
    Returns the due date
    """
    return datetime.today() + timedelta(days=7)

class IssueBook(models.Model):
    """
    Models issue book transaction storing infor about a book and borower
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    due_date = models.DateField(default=expiry)

    def __str__(self):
        """
        Returns readable string representing the issue transaction
        """
        return self.book.book_title + ' issued for ' +\
                self.member.first_name + ' ' + self.member.last_name


class ReturnBook(models.Model):
    """
    Models return book trasaction of a returned book
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return readable string representing the ReturnBook model
        """
        return self.book.book_title + ' is returned by ' +\
                self.member.first_name + ' ' + self.member.last_name
