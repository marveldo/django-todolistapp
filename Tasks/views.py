from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdatedForm,Taskform
import json



@login_required(login_url='login')
def home (request):
    profile = request.user.profile
    if request.GET.get('Search'):
        search = request.GET.get('Search')
    else:
        search = ''
    tasks = profile.task_set.filter( name__icontains = search)
    context = {'profile':profile , 'tasks': tasks, 'search' : search}
    return render(request,'Tasks/home.html', context )

def loginuser(request):
    if request.user.is_authenticated :
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        try:
            user = User.objects.get(username = username)
        except :
            print('username does not exist')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            print('username not correct')


    return render(request,'Tasks/login.html')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserUpdatedForm()
    if request.method == 'POST':
        form = UserUpdatedForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'Tasks/register.html',context)


@login_required(login_url= 'login')
def  Createtask(request):
    profile = request.user.profile
    form = Taskform()
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.profile = profile
            task.save()
            return redirect('home')
    context = {'form': form}        
    return render(request,'Tasks/createtask.html', context)
@login_required(login_url='login')
def Edittask(request,pk):
    profile = request.user.profile
    task = profile.task_set.get(id = pk)
    form = Taskform(instance = task)
    if  request.method == 'POST':
        form = Taskform(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request,'Tasks/createtask.html', context)
@login_required(login_url='login')
def deleteprojects(request):
    profile =  request.user.profile
    data = json.loads(request.body)
    taskid = data['id']
    action = data['action']
    task = profile.task_set.get(id = taskid)
    if action == 'delete':
        task.delete()
    

    return JsonResponse('Project deleted succesfully', safe=False)
@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')