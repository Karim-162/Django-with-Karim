from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'name':'shafayet',
        'age':23,
        'nationality':'bangladeshi',
    }
    #return HttpResponse('<h1>hi welcome</h1>')
    #return render(request,'index.html',{'name':name})
    return render(request,'index.html',context)
