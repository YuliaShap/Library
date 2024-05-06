from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from authentication.views import librarian_required
from author.models import Author
from .forms import AuthorForm
   

@librarian_required
def authors(request):
    authors_list = Author.objects.all()
    return render(request, 'author/main.html', {'authors_list': authors_list})
def new_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'author/new_author.html', {'form': form})


@librarian_required
def remove_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)

    if request.method == 'POST':
        if Author.delete_by_id(author_id):
            return redirect('authors')
        else:
            return HttpResponseForbidden("Author is associated with books and cannot be deleted.")

    return render(request, 'author/remove_author.html', {'author': author})
