from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import TeacherRegistrationForm
from users.models import UserInfo, User, OtherRequests
from posts.models import Post, PostLikes, Comments
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.


def teacher_login(request):
    if request.user.is_authenticated:
        return redirect('teacher_dashboard')

    else:
        return render(request, "teachers/teacher_login.html")


def teacher_register(request):


    if request.user.is_authenticated:
        user_type = UserInfo.objects.get(user=request.user)

        if user_type.is_student == True:
            messages.warning(request, "You are logged in as a student and trying to access teacher's portal")
            return redirect('dashboard')

        else:
            return redirect('teacher_dashboard')


    form = TeacherRegistrationForm()
    
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')

            messages.info(request, f"Account created for{username}")

            new_user = authenticate(username = form.cleaned_data.get('username'),
                                    password = form.cleaned_data.get('password1'))
            
            login(request, new_user)

            user_profile = UserInfo.objects.create(user=request.user, is_teacher = True, is_student = False)
            user_profile.save()
            
            return redirect('teacher_dashboard')
        
        else:
            return redirect('teacher_register')

    
    else:

        return render(request, "teachers/teacher_register.html", {'form':form})

@login_required(login_url='teacher_login')
def teacher_dashboard(request):
    user_type = UserInfo.objects.get(user=request.user)
    if user_type.is_student == True:
        messages.warning(request, "You are logged in as a student and trying to access teacher's portal")
        return redirect('dashboard')
    
    else:
        #posts = Post.objects.all().order_by('-id')
        likes = PostLikes.objects.filter(user=request.user)

        p = Paginator(Post.objects.all().order_by('-id'), 8)
        page = request.GET.get('page')
        posts = p.get_page(page)

        comments = Comments.objects.all()

        return render(request, "teachers/teacher_dashboard.html", {'user_type':user_type, 'posts':posts
                        ,'likes':likes, 'comments':comments})


@login_required(login_url='teacher_login')
def teacher_profile(request,u):
    user_type = UserInfo.objects.get(user=request.user)
    if user_type.is_student == True:
        messages.warning(request, "You are logged in as a student and trying to access teacher's portal")
        return redirect('dashboard')
    
    else:
        return render(request, "teachers/teacher_profile.html", {'user_type':user_type})


@login_required(login_url='teacher_login')
def teacher_settings(request):
    user_type = UserInfo.objects.get(user=request.user)
    if user_type.is_student == True:
        messages.warning(request, "You are logged in as a student and trying to access teacher's portal")
        return redirect('dashboard')
    
    else:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                user = request.user.username
                address = request.POST['address']
                contact = request.POST['contact']
                image = user_type.profile_img

                user_type.address = address
                user_type.contact = contact
                user_type.profile_img = image

                user_type.save()

                messages.success(request, f"Information saved")

                return redirect(f'/teacher_profile/{user_type.user}')
            

            
            else:
                user = request.user.username
                address = request.POST['address']
                contact = request.POST['contact']
                image = request.FILES.get('image')

                user_type.user = request.user
                user_type.address = address
                user_type.contact = contact
                user_type.profile_img = image

                user_type.save()

                messages.success(request, f"Information saved")

                return redirect('teacher_settings')

        return render(request, "teachers/teacher_settings.html", {'user_type':user_type})
    


@login_required(login_url='teacher_login')
def teacher_requests(request):
    user_type = UserInfo.objects.get(user=request.user)
    if user_type.is_student == True:
        messages.warning(request, "You are logged in as a student and trying to access teacher's portal")
        return redirect('dashboard')
    
    else:
        get_requests = OtherRequests.objects.all().order_by('-id')

        if request.method == 'POST':
            response = request.POST['response']
            request_id = request.POST['request_id']

            request_model = OtherRequests.objects.get(id=request_id)
            request_model.response = response
            request_model.has_responded = True
            request_model.save()

            return render(request, "teachers/teacher_requests.html", {'user_type':user_type, 'get_requests':get_requests})


        return render(request, "teachers/teacher_requests.html", {'user_type':user_type, 'get_requests':get_requests})


