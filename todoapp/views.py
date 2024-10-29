from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from todoapp.forms import TodoForm
from todoapp.models import Todo

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/signup.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'todoapp/signup.html', {'form':UserCreationForm(), 'error':'That user name has already been taken'})
                
        else:
            return render(request, 'todoapp/signup.html', {'form':UserCreationForm(), 'error':'Password did not match'})
        
        
        
def home(request):
     return render(request, 'todoapp/home.html')
 
 
def logoutuser(request):
     if request.method == "POST":
         logout(request)
         return redirect('home')
     
def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todoapp/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todoapp/login.html', {'form':AuthenticationForm(),'error': 'username or password did not match'})
        else:
            login(request, user)
            return redirect('home')
        
        

def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todoapp/create.html', {'form':TodoForm()})
    else:
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('todo_list')
    
def todoList(request):
    todos = Todo.objects.filter(user = request.user,datecompleted__isnull=True)
    message = "No pending todos found." if not todos else None  # Check if the list is empty
    context = {
        'todos': todos,
        'message': message,
    }
    return render(request, 'todoapp/todo_list.html', context)

def todopage(request, id):
    todo = get_object_or_404(Todo, pk = id, user=request.user)
    context = {'todos':todo}
    
    if request.method == "GET":
        form = TodoForm(instance=todo)
        context = {'todo':todo, "form":form}
        return render(request, 'todoapp/todo_page.html', context)
    else:
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('todo_list')
        
        
def complete(request):
    todo = Todo.objects.filter(user = request.user)
    # if todo.status == 'complete':
    #     todo.save()
    context = {'todo': todo}
    return render(request, 'todoapp/completed.html', context)


def deletetodo(request, id):
    todo = get_object_or_404(Todo, pk=id, user=request.user)
    print(todo.pk)
    print(todo.user)
    if request.method == "POST":
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todoapp/todo_list.html')
    
    