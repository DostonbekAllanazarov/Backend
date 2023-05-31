from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    image = forms.FileField()
    def __init__(self, *args, **kwargs):
       super().__init__(*args,**kwargs)
       self.fields['image'].widget.attrs.update({
            'onchange':"document.getElementById('image').src=window.URL.createObjectURL(this.files[0])",
            'style':'display:none',
            'id':'file',
       })
       self.fields['username'].widget.attrs.update({
            'placeholder':'username'
       })
       self.fields['email'].widget.attrs.update({
            'placeholder':'Email'
       })
       self.fields['password1'].widget.attrs.update({
            'placeholder':'password1'
       })
       self.fields['password2'].widget.attrs.update({
            'placeholder':'confirm password'
       })
       for key, field in self.fields.items():
           field.label = ""
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2','image']