from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    # feature1=Feature()
    # feature1.id=0
    # feature1.name="Fast"
    # feature1.details='service is very quick'
    
    # feature2=Feature()
    # feature2.id=1
    # feature2.name="Reliable"
    # feature2.details='service is very Reliable'
    
    # feature3=Feature()
    # feature3.id=2
    # feature3.name="Easy to Use"
    # feature3.details='service is User Friendly'
    
    # feature4=Feature()
    # feature4.id=3
    # feature4.name="affordable"
    # feature4.details='service is budget friendly for everyone'

    # feature5=Feature()
    # feature5.id=4
    # feature5.name="dd"
    # feature5.details='dd'

    # features=[feature1,feature2,feature3,feature4,feature5]
    #print(len(features))  # 4 আসা উচিত
    #return HttpResponse('<h1>hi welcome</h1>')
    #return render(request,'index.html',{'name':name})

    features = Feature.objects.all() 
    return render(request,'index.html',{'features': features})

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request,'email is already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username is already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password, email=email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password not matched')
            return redirect('register')
    else:
        return render(request,'register.html')