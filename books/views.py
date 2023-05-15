# views.py
from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect


def author_create(request):
    if request.method == 'POST':

        data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect('author-list')
        else:
            errors = serializer.errors
    else:
        errors = None

    return render(request, 'author-create.html', {'errors': errors})


class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        authors = self.get_queryset()
        return render(request, 'author_list.html', {'authors': authors})


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        author = self.get_object()
        return render(request, 'author_detail.html', {'author': author})


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'email']
    template_name = 'author_update.html'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author-list')
    template_name = 'author-delete.html'
