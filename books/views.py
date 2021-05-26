from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):  # mixing are loaded from left to right so LoginRequiredMixin should be first
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'  # for traditional django authentication system login_url = 'login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    permission_required = 'books.special_status'  # custom permission created in Meta class in models.py
