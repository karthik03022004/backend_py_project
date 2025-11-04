from django.urls import path
from . import views
urlpatterns=[
    path('create/',view=views.create_user),
    path('read/',view=views.read_user),
    path('update/<int:mid>',view=views.update_user),
    path('delete/<int:mid>',view=views.delete_user)
]