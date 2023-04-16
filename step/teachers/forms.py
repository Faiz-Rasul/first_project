from django import forms
from django.contrib.auth.models import User
from users.forms import UserRegistrationForm


class TeacherRegistrationForm(UserRegistrationForm):
    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-input' , 'placeholder': 'Enter your email'})
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
    def __init__(self, *args, **kwargs):
        super(TeacherRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Enter your password again'})            
