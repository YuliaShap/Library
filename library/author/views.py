from statistics import StatisticsError
import statistics
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets

from requests import Response

from authentication.views import librarian_required
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .forms import AuthorForm
from .models import Author
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
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


