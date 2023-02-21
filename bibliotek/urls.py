from django.urls import path

from . import views

urlpatterns = [
    path('author/create/', views.AuthorCreateView.as_view()),
    path('author/list/', views.AuthorListView.as_view()),
    path('author/<pk>/', views.AuthorView.as_view()),
    path('books/create/', views.BooksCreateView.as_view()),
    path('books/list/', views.BooksListView.as_view()),
    path('books/<pk>/', views.BooksView.as_view()),
    path('readers/create/', views.ReadersCreateView.as_view()),
    path('readers/list/', views.ReadersListView.as_view()),
    path('readers/<pk>/', views.ReadersView.as_view()),
]
