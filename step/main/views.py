from django.shortcuts import render, redirect
from django.http import HttpResponse




# Create your views here.
def index(request):


    if request.user.is_authenticated:
        return redirect('dashboard')

    else:    
        return render(request, 'main/index.html')



