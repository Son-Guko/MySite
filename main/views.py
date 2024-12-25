from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from main.forms import Createnewlist , DocumentForm

# Create your views here.
def index(request, id):
    list = ToDoList.objects.filter(id=id)
    lists = ToDoList.objects.all()
    if request.method == 'POST':
        if request.POST.get("save"):
            for item in list.item_set.all():
                if request.POST.get("c" + str(item.id))  == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif request.POST.get("newItem"):
            txt = request.POST.get("new")
            if len(txt) > 2:
                list.item_set.create(text = txt, complete = False)
            else:
                print("Invalid Item")
    return render(request, 'home\index.html', {'list':list, 'lists':lists})

def home(request):
    return render(request, 'base.html')

def create(request):
    if request.method == "POST":
        form = Createnewlist(request.POST)
        if form.is_valid():
            m = form.cleaned_data["name"]
            t = ToDoList(name= m)
            t.save() 
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = Createnewlist()
    return render(request, 'home\create.html', {'form':form})


def upload_file(request): 
    if request.method == 'POST': 
        form = DocumentForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('upload_file') 
    else: form = DocumentForm() 
    
    return render(request, 'upload.html', {'form': form})