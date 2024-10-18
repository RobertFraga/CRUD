from django.shortcuts import render, redirect
from .models import User


def views(request):
    users = User.objects.all()
    return render(request, 'index.html', {'inserted':users})


#insert
def addForm(request):
    return render(request, 'addform.html')
def insertForm(request):
    insertFName = request.POST['FirstName'];
    insertLName = request.POST['LastName'];
    add = User(first_name = insertFName, second_name = insertLName)
    add.save()
    return redirect('/')


#delete
def deleteRecord(request, pk):
    users = User.objects.filter(user_id = pk)
    users.delete()
    return redirect('/')

#edit
def viewEdit(request, pk):
    users = User.objects.get(user_id = pk)
    return render(request, 'editRecord.html', {'User': users})

def update(request, pk):
    newFName = request.POST['FirstName']
    newLName = request.POST['LastName']

    users = User.objects.get(user_id = pk)

    users.first_name = newFName
    users.second_name = newLName
    users.save()
    return redirect('/')
    