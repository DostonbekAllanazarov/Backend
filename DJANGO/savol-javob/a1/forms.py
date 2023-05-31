from django.forms import ModelForm
from .models import Questions, Answers


class FormQuestion(ModelForm):
    class Meta:
        model = Questions
        fields = ['user','theme']    


class FormAnswer(ModelForm):
    class Meta:
        model  = Answers
        fields = '__all__'