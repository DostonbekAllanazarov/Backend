from django.shortcuts import render,redirect

# Create your views here.
from .forms import FormAnswer,FormQuestion
from .models import Questions, Answers
from django.contrib.auth.models import User
def room(request,id):
    question = Questions.objects.get(id=id)
    answers = Answers.objects.filter(question=question)
    form = FormAnswer()
    if request.method == 'POST':
        answer = request.POST.get('answer')
        Answers.objects.create(
            user = request.user,
            question = question,
            answer = answer,    
        ) 
    context = {
        'question':question,
        'form':form,
        'answers':answers,
    }
    return render(request, 'room.html', context)

def home(request):
    question = Questions.objects.all()
    context = {
        'questions':question,
    }
    return render(request, 'home.html', context)

def topic(request):
    form = FormQuestion()
    if request.method == 'POST':
       theme = request.POST.get('theme')
       form = Questions(user = request.user,
       theme = theme,
       )
       form.save()
       return redirect('home')    
    context = {
        'form':form
    }    
    return render(request, 'topic.html', context)