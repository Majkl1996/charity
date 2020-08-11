from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from .models import Category, Institution

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def LandingPage(request):
    return render(request, 'index.html')

def AddDonationPage(request):
    categories = Category.objects.all().order_by('id')
    institutions = Institution.objects.all().order_by('id')
    return render(request, 'form.html', locals())

def LoginPage(request):
    return render(request, 'login.html')

def RegisterPage(request):
    if request.method == "POST":
        if form.is_valid():
            password1 = request.form.get('password')
            password2 = request.form.get('password2')
            if password1 == password2:
                new_user = User()
                new_user.username = request.form.get('email')
                new_user.first_name = request.form.get('name')
                new_user.last_name = request.form.get('surname')
                new_user.password = request.form.get('password')
                new_user.save()
                return redirect('login')
            else:
                messages.info(request, 'Podane hasła są różne')
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')
