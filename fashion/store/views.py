from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserFrom
from django import forms
from .models import Product,Category

def category_summary(reguest):
    categories = Category.objects.all()
    return render(reguest, 'category_summary.html', {"categories": categories})


def category(request, foo):
    # Retrieve the category based on the slug
    category = Category.objects.get(name = foo)

    # Retrieve all products associated with the category
    products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category.html', context)
    
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render (request, 'product.html',{'product':product})

def home(request):
    products = Product.objects.all()
    return render (request, 'home.html',{'products':products}) 

def about(request):
    return render (request, 'about.html',{})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You have been logged in'))
            return redirect('home')
        else:
            messages.success(request,('Error logging in, Please try again'))
            return redirect('login')
    else:
        return render (request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('login')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,('You have been registered Successfully'))
            return redirect('home')
        else:
            messages.success(request,('Error registering, Please try again'))
            return redirect('register')
    else:
        return render (request, 'register.html',{'form':form})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserFrom(request.POST or None, instance = current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request,"User Has Been Updated!!")
            return redirect('home')
        return render(request,"update_user.html", {'user_form': user_form})
    else:
        messages.success(request,"You Must Be Logged In This Page!!")
        return redirect('home')
