from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def offer(request):
    return render(request, 'offer.html')


def about(request):
    return render(request, 'about.html')


def care(request):
    return render(request, 'care.html')


def codes(request):
    return render(request, 'codes.html')


def contact(request):
    return render(request, 'contact.html')


def faqs(request):
    return render(request, 'faqs.html')


def hold(request):
    return render(request, 'hold.html')


def kitchen(request):
    return render(request, 'kitchen.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Exists')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email,
                                                password=password)
                user.save()
                return redirect('login')
        else:
            if User.objects.filter(username=username).exists():
                messages.info('Password Not Matching')

    return render(request, 'register.html')


def shipping(request):
    return render(request, 'shipping.html')


def single(request):
    return render(request, 'single.html')


def terms(request):
    return render(request, 'terms.html')


def wishlist(request):
    return render(request, 'wishlist.html')