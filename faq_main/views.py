from django.shortcuts import  render, redirect
from django.utils import timezone
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from apps.questions.models import Answer, Question
from datetime import timedelta

@login_required(login_url='login/')
def homepage(request):
    time_threshold = timezone.now() - timedelta(days=7)
    questions = Question.objects.filter(created_date__gt=time_threshold).order_by('-created_date')
    return render(request=request, template_name='home.html', context={'questions':questions})

@login_required(login_url='login/')
def details(request, question_id):
    record = Answer.objects.get(question__pk=question_id)
    return render(request=request, template_name='details.html', context={'record':record})

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        messages.warning(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.warning(request,"Invalid username or password.")
        else:
            messages.warning(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("homepage")

@login_required(login_url='login/')
def currency(request):
    return render(request=request, template_name="currency.html")