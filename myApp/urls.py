from django.urls import path
from .import views

urlpatterns = [
    path('', views.views, name='home'),
    
    #insert
    path('addform/', views.addForm, name="addform"),
    path('insert/', views.insertForm, name='insert'),


    #delete
    path('deleteRecord/<int:pk>', views.deleteRecord, name='deleteRecord'),

    #edit
    path('viewEdit/<int:pk>', views.viewEdit, name='viewEdit'),
    path('update/<int:pk>', views.update, name='update')
]
