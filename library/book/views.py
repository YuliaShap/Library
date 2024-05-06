from django.contrib.auth import get_user
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, get_object_or_404

from authentication.views import librarian_required
from .forms import BookForm
from .models import Book


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
