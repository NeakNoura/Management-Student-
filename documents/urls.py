from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_document, name='add_document'),
    path('document/<int:pk>/', views.document_detail, name='document_detail'),
    path('add/', views.document_list, name='document_list'),

]
