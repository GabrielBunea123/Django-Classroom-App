from django.shortcuts import render,redirect
from .models import Room,Joined,Upload_Task,UploadFiles,Comments,Topic,UploadTaskFiles,Mark
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
import random
from random import choice
from .forms import TaskForm,FileFieldForm
import datetime
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy,reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='login')
def home_page(request):#the room with the joined rooms
    current_user = request.user.id
    all_rooms = Joined.objects.filter(user = current_user)
    
    return render(request,'home_page.html',{'all_rooms':all_rooms})

@login_required(login_url='login')
def join_room(request):
    return render(request, 'join_room.html',{})#te inscrii in clasa


@login_required(login_url='login')
def room(request,room):#pentru sectiunea stream
    if request.method == 'GET':
        username = request.GET.get('username')
        stream = request.GET.get('stream')
        classwork = request.GET.get('classwork')
        room_details = Room.objects.get(code=room)#camera
        tasks = Upload_Task.objects.filter(room_code = room)#get all the tasks for the specified room
        room_name = room_details.name#numere camerei
        current_user = request.user.id

        details = {'username':username,'room_details':room_details,
        'room':room,'room_name':room_name,'tasks':tasks,'current_user':current_user,
        'stream':stream,'classwork':classwork}
        return render(request, 'room.html',details)
    else:
        return render(request, 'room.html',)

@login_required(login_url='login')
def room_classwork(request,room):#pentru  sectiunea classwork unde sunt ordonate taskurile
    if request.method =="GET":
        username = request.GET.get('username')
        stream = request.GET.get('stream')
        classwork = request.GET.get('classwork')
        room_details = Room.objects.get(code=room)
        tasks = Upload_Task.objects.filter(room_code = room)#get all the tasks for the specified room
        topic = Topic.objects.filter(room=room)
        room_name = room_details.name
        current_user = request.user.id

        details = {'username':username,'room_details':room_details,
        'room':room,'room_name':room_name,'tasks':tasks,'current_user':current_user,'topic':topic,
        'stream':stream,'classwork':classwork}
        return render(request, 'room_classwork.html',details)
    else:
        return render(request, 'room_classwork.html')

@login_required(login_url='login')
def checkview(request):
    username = request.POST['username']
    room = request.POST['room_name']
    current_user = request.user
    if Room.objects.filter(code = room).exists():#daca camera exista si userul nu a mai fost in ea, sa l inscrie si sa apara pe ecranul acasa
        if not Joined.objects.filter(user=current_user,classroom_code=room).exists():
            correct_room = Room.objects.get(code = room)
            Joined.objects.create(user=current_user,classroom_code=room,classroom_name=correct_room.name,classroom_color = correct_room.color)
            return redirect('/room/'+room)
    else:
        messages.info(request, "This room does not exits!")
        return redirect('home_page')

@login_required(login_url='login')
def create_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')#name
        gen = request.POST.get('gen')#submit btn
        colorChoices = ['#3066BE','#59A96A','#0d6efd','#4E878C','#5CA4A9','#DB3A34', '#177E89','#eda207']
        color = random.choice(colorChoices)

        password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*-_=+') for i in range(10)])
        if Room.objects.filter(code=password).exists() == False and name!='': #daca camera nu exista si numele nu este egal cu nimic atunci se creeaza clasa si user ul este inscris automat in ea
            Room.objects.create(name=name,code=password,color=color,author = request.user)
            Joined.objects.create(user=request.user,classroom_code=password,classroom_name=name, classroom_color = color)
        return render(request,'create_room.html',{"password":password})
    else:
        return render(request,'create_room.html',{})

@login_required(login_url='login')
def create_task(request, *args, **kwargs):
    code = kwargs['room']
    if request.method=='POST':
        title = request.POST.get('title')
        topic = request.POST.get('topic')
        task = request.POST.get('task')
        files = request.FILES.getlist('myfile')#the image
        max_points = request.POST.get("max")#maximum points
        due_date = request.POST.get('date')
        submit = request.POST.get('submit')
        form = FileFieldForm(request.POST)

        if submit:
            task_create = Upload_Task.objects.create(title=title,task=task,room_code=code,date = datetime.date.today(),author = request.user,max_points = max_points,due_date=due_date,topic=topic)
            task_create.save()#daca se apasa pe submit, se creeaza task ul  
            for i in files:#fisiere din task sunt adaugate cu task_number ul egal cu id ul taskului
                UploadTaskFiles.objects.create(file=i,task_number=task_create.id)
        # return render(request,'create_task.html',{'submit':submit,'form':form})
        return redirect('/room/'+code)
    else: 
        current_user = request.user.id
        room_details = Room.objects.get(code=code)
        if current_user==room_details.author.id:
            return render(request,'create_task.html',{current_user:current_user,room_details:room_details})
        else: return HttpResponse("You are not allowed")

@login_required(login_url='login')
def task(request,pk):
    comment = request.POST.get('message')
    submit = request.POST.get('submit')

    submitFiles = request.POST.get("mySubmitButton")
    toAddFiles = request.FILES.getlist('file_field') #the added files by the user that are about to be turned in

    task = Upload_Task.objects.get(id = pk)
    files = UploadTaskFiles.objects.filter(task_number=pk) #the files posted by the teacher
    room = Room.objects.get(code = task.room_code)
    mark = Mark.objects.filter(user=request.user,task_number=pk)
    if submit:#daca se adauga comentarii
        Comments.objects.create(value=comment,date=datetime.datetime.now(),author =request.user,task_id=pk)
    if submitFiles:
        for f in toAddFiles:#pentru a incarca temele
            UploadFiles.objects.create(file=f,author=request.user,task_number=pk,room_code=task.room_code)
    messages = Comments.objects.filter(task_id=pk)
    returned_files = UploadFiles.objects.filter(task_number=pk)
    if mark.exists():   
        return render(request,'task.html',{'task':task,'files':files,'room':room,'messages':messages,'returned_files':returned_files,'mark':mark[0].mark})
    return render(request,'task.html',{'task':task,'files':files,'room':room,'messages':messages,'returned_files':returned_files})

@login_required(login_url='login')
def returned(request,pk):
    students_files = UploadFiles.objects.filter(task_number=pk)

    if students_files.exists():
        room_code = students_files[0].room_code
        joined = Joined.objects.filter(classroom_code =room_code)#totii elevi care au returnat tema 
        return render(request,'returned.html',{'students_files':students_files,'joined':joined,'pk':pk,'host':request.user})
    else: return HttpResponse("No student returned this homework")


@login_required(login_url='login')
def returned_details(request,pk,string):
    files = UploadFiles.objects.filter(task_number=pk,author__username=string)# detalii despre fiecare tema a fiecarui elev
    for i in files:
        code = i.room_code
        task = i.task_number

    submit = request.GET.get('submit')
    if(submit):
        room = Room.objects.get(code = code)
        mark = request.GET.get('mark')
        user = User.objects.get(username = string)
        Mark.objects.create(user=user,classroom_code=code,classroom_name=room.name,mark=mark,task_number=task)
        return redirect('home_page')
    return render(request,'returned_details.html',{'files':files, 'username':string})
    

@login_required(login_url='login')
def add_topic(request,room):
    submit = request.POST.get('submit')
    topic_name = request.POST.get('topic')
    if submit:#adaugarea unui topic
        Topic.objects.create(name=topic_name,room=room,author=request.user)

    return render(request,'add_topic.html',{})

class AddMoreFiles(FormView):
    model = UploadTaskFiles
    form_class = FileFieldForm
    # success_url = reverse('task', args=[str(task_id)]) # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        # task_number = self.kwargs['pk']
        # task = UploadTaskFiles.objects.get(task_number = self.kwargs['pk'])
        if form.is_valid():
            for f in files:
                UploadTaskFiles.objects.create(file=f,task_number=self.kwargs['pk'])#pe pagina de task, daca profesorul vrea sa mai incarce fisiere, asa se poate creea feature ul
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def get_success_url(self,*args, **kwargs):
        return reverse('task',args=[self.kwargs['pk']])#returns the page with the old pk

def my_grades(request):
    my_classes = Joined.objects.filter(user = request.user)
    for i in my_classes:
        code = i.classroom_code
    marks = Mark.objects.filter(user=request.user)
    print(marks)
    return render(request,"my_marks.html",{'my_classes':my_classes,'marks':marks})

