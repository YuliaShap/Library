import statistics
from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, get_object_or_404
from requests import Response

from authentication.views import librarian_required
from .forms import BookForm
from .models import Book

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(RetrieveUpdateDestroyAPIView):
  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=statistics.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
def book(request):
    user = get_user(request)
    if isinstance(user, AnonymousUser):
        return redirect('/authentication/login/')
    else:

        books_list = []
        books = Book.get_all()
        for book in books:
            authors = book.authors.all()
            authors_name = ', '.join([f"{author.name} {author.surname}" for author in authors])
            books_list.append({
                "id": book.id, "name": book.name, "description": book.description, "count": book.count,
                "authors_name": authors_name,
                "year_of_publication": book.year_of_publication, "date_of_issue": book.date_of_issue
            })

        if user.role == 0:
            return render(request, 'book/book.html', {'books': books_list, 'active_page': 'books', 'role': user.role})
        elif user.role == 1:
            return render(request, 'book/book.html', {'books': books_list, 'active_page': 'books', 'role': user.role})
        else:
            return render(request, 'book/book.html', {'books': [], 'active_page': 'books'})


def book_info(request, book_id):
    if request.method == "GET":
        book = Book.get_by_id(book_id=book_id)
        authors = book.authors.all()
        authors_name = ', '.join([f"{author.name} {author.surname}" for author in authors])
        year_of_publication = book.year_of_publication
        date_of_issue = book.date_of_issue
        return render(request, 'book/book_details.html', {'book': book, 'author': authors_name,
                                                          'year_of_publication': year_of_publication,
                                                          'date_of_issue': date_of_issue})


@librarian_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_info', book_id=book_id)
    else:
        form = BookForm(instance=book)

    return render(request, 'book/edit_book.html', {'form': form, 'book': book})
