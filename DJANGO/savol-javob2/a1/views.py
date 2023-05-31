from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Question, Answer, Profile
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.

def logoutPage(request):
    logout(request)
    return redirect('home')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {})
    

def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            image = form.cleaned_data['image']
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                # User is authenticated
            u = User.objects.get(username=username)
            profile = Profile.objects.create(
                user = u,
                image = image
            )
            profile.save()
            return redirect('home')
        else:
            print("Wrong")    
    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)
    
@login_required
def answer(request,id):
    allquestions = Question.objects.all()
    question = Question.objects.get(id=id)
    if request.method == 'POST':
        pr = Profile.objects.get(user = request.user)
        answer = request.POST.get('answer')
        form = Answer.objects.create(
            user = pr,
            question = question,
            answer = answer,
        )
        form.save()
    answers = Answer.objects.filter(question=question)    
    context = {
        'question':question,
        'answers':answers,
        'allquestions':allquestions,
    }
    return render(request, 'room.html', context)
    
@login_required
def question(request):
    if request.method == 'POST':
        question = request.POST.get('savol')
        pr = Profile.objects.get(user = request.user)
        form = Question.objects.create(
            user = pr,
            question = question,
        )
        form.save()
        return redirect('home')

    return render(request, 'question.html', {})
    

def home(request):
    questions = Question.objects.all()
    context = {
        'questions':questions,
    }
    return render(request, 'home.html', context)
    