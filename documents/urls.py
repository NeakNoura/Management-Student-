from django.urls import path
from . import views

urlpatterns = [
    path('documents/', views.document_list, name='document_list'),
    path('documents/document/<int:pk>/', views.document_detail, name='document_detail'),
    path('documents/add/', views.add_document, name='add_document'),
    path('', views.home, name='home'),  # Home page (optional)
]
