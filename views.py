
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'judul':'Dalmore Planner',
        'sub judul':'selamat datang'
    }
    return render(request,'index.html',context)

# method view
def index2(request):
    return HttpResponse("<h1>Hallo ini Home</h1>")