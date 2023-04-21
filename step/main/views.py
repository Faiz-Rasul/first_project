from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import UserInfo
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):


    if request.user.is_authenticated:
        user_obj = UserInfo.objects.get(user=request.user)

        if user_obj.is_student == True:
            return redirect('dashboard')

        elif user_obj.is_teacher == True:
            return redirect('teacher_dashboard')

    else:    
        return render(request, 'main/index.html')

@login_required(login_url='index')
def user_type(request):
    user_info = UserInfo.objects.get(user = request.user)

    if user_info.is_teacher == True:
        user_type = 'teacher'

    else:
        user_type = 'student' 
        
    return render(request, 'main/user_type.html', {'user_type':user_type})



