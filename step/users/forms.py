from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Voting

class UserRegistartionForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class VoteForm(forms.Form):

    option1 = Voting.objects.get(id=8)
    option1 = option1.option

    option2 = Voting.objects.get(id=9)
    option2 = option2.option

    option3 = Voting.objects.get(id=10)
    option3 = option3.option

    option4 = Voting.objects.get(id=11)
    option4= option4.option

    option5 = Voting.objects.get(id=13)
    option5 = option5.option

    option6 = Voting.objects.get(id=14)
    option6 = option6.option

    option7 = Voting.objects.get(id=16)
    option7 = option7.option

  
    vote = forms.CharField(widget=forms.RadioSelect(choices=[(option1, option1),(option2, option2),(option3, option3),(option4, option4),(option5, option5),(option6, option6), (option7, option7)]))




