# urls.py

from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorRetrieveUpdateDestroyView,
    author_create,
    AuthorUpdateView,
    AuthorDeleteView,
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyView.as_view(), name='author-detail'),
    path('authors/create/', author_create, name='author-create'),  # Update this line
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]
