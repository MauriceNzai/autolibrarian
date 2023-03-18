"""
This module registers all models
"""
from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Book, IssueBook, ReturnBook, Member
from .models import LibUser

# Register your models here.
admin.site.register(Session)

admin.site.register(LibUser)

class BookAdmin(admin.ModelAdmin):
    """
    Admin class for the Book model
    """
    list_display=("user","book_id","book_title","subject","category")
admin.site.register(Book, BookAdmin)

class IssueBookAdmin(admin.ModelAdmin):
    """
    Admin class for the IssueBook model
    """
    list_display=("user","book","member")
admin.site.register(IssueBook, IssueBookAdmin)

class ReturnBookAdmin(admin.ModelAdmin):
    """
    Admni class for the ReturnBook model
    """
    list_display=("user","book")
admin.site.register(ReturnBook, ReturnBookAdmin)

class MemberAdmin(admin.ModelAdmin):
    """Admin class for the Member model
    """
    list_display=("user", "first_name", "last_name", "member_id")
admin.site.register(Member, MemberAdmin)
