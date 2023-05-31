from django.shortcuts import render,redirect

# Create your views here.
from .models import Question, Answer
from .forms import RegisterForm

def Register(request):
    form  = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'signup.html', context)

def room(request, id):
    question = Question.objects.get(id=id)
    answers = Answer.objects.filter(question=question).order_by('-id')
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if not Answer.objects.filter(answer = answer).exists():
            form = Answer(
            user = request.user,
            question = question,
            answer = answer,
            )
            form.save()
    context = {
        'question':question,
        'answers':answers,
    }
    return render(request, 'room.html', context)

def topic(request):
    if request.method == 'POST':
        if not Question.objects.filter(question = request.POST.get('question')).exists():
           question = request.POST.get('question')
           form = Question(
            user = request.user,
            question = question,
           )
           form.save()
           return redirect('home')
    context = {
           
    }
    return render(request, 'topic.html', context)

def home(request):
    questions = Question.objects.all().order_by('-id')
    if request.method == 'POST':
        question = request.POST.get('question')
        form = Question(
            user = request.user,
            question = question,
        )
        form.save()
    context = {
       'questions':questions,    
    }
    return render(request, 'index.html', context)