from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="books_index"),
    path("show/<int:id>", views.show, name="show"),
    
    path("new", views.new, name="new"),
    path("create", views.create, name="create"),
    
    path("edit/<int:id>", views.edit, name="edit"),
    path("update/<int:id>", views.update, name="update"),
    
    path("delete/<int:id>", views.delete, name="delete"),
]