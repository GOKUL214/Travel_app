from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from requests import request
def demo(request):
    return render(request,'index.html')
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first = request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                print('invalid username')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                print('invalid email')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first, last_name=last, email=email, password=pass1 )
                user.save()

                # print('successful')
                return redirect('login')
        else:
            messages.info(request,"password not matched")
            print('invalid password')
            return redirect('register')


        return redirect('/')




    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

