from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Voting

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class VoteForm(forms.Form):

    option1 = Voting.objects.get(id=1)
    option1 = option1.option

    option2 = Voting.objects.get(id=2)
    option2 = option2.option

    option3 = Voting.objects.get(id=3)
    option3 = option3.option

    option4 = Voting.objects.get(id=4)
    option4= option4.option

    option5 = Voting.objects.get(id=5)
    option5 = option5.option

    option6 = Voting.objects.get(id=6)
    option6 = option6.option

    option7 = Voting.objects.get(id=7)
    option7 = option7.option

  
    vote = forms.CharField(widget=forms.RadioSelect(choices=[(option1, option1),(option2, option2),(option3, option3),(option4, option4),(option5, option5),(option6, option6), (option7, option7)]))



