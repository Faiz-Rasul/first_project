from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegistrationForm, VoteForm
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime
from django.contrib.auth import authenticate, login
from .models import OtherRequests, UserInfo, AvailableCourses, Enrollment, Fees, Voting,  UserVotes
from posts.models import Post, PostLikes, Comments
from django.db.models import Q
from django.contrib.auth.models import User
import random
from django.core.paginator import Paginator


# Create your views here.

def register(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  

        if form.is_valid():
            username = form.cleaned_data.get('username')


            new_user = form.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            degree_title = ['bscs', 'bba', 'bms', 'bfd']

            student_degree_title = random.choice(degree_title)
            
            user_model = User.objects.get(username=username)

            new_profile = UserInfo.objects.create(user=user_model, degree_title=student_degree_title)
            new_profile.save()



            new_user_fees = Fees.objects.create(user=user_model, enrollment_fees=5000, monthly_fees = 2000, balance=7000)
            new_user_fees.save()
            
            messages.success(request, f"Account created for {username}")

            return redirect('dashboard')
        
        else:
            form = UserRegistrationForm()
            messages.warning(request, f'Please enter the correct information')
        return render(request, 'users/register.html', {'form': form })
    
    return render(request, 'users/register.html', {'form': form })

@login_required(login_url='student_login')
def dashboard(request):
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()



        fees_object = Fees.objects.get(user=request.user)
        likes = PostLikes.objects.filter(user=request.user)
        comments = Comments.objects.all()

        p = Paginator(Post.objects.all().order_by('-id'), 8)
        page = request.GET.get('page')
        posts = p.get_page(page)

        current_time = now.strftime("%H:%M:%S")
        
        return render(request, 'users/dashboard.html', {'today':today, 'current_time': current_time, 
        'user_profile':user_profile, 'fees_object':fees_object, 'posts':posts, 'likes':likes,
        'comments':comments,})

@login_required(login_url='student_login')
def request(request):

    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")


        if request.method == 'POST':

            username = request.POST['username']
            subject = request.POST['subject']
            content = request.POST['content']

            new_request = OtherRequests.objects.create(user= username, subject=subject, content=content)
            new_request.save()



            messages.success(request, f"Your request has been sent!")
            return redirect('request')
            

        
        return render(request, 'users/request.html', {'user_profile': user_profile, 'today':today, 'current_time': current_time})


@login_required(login_url='student_login')
def view_requests(request):

    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")


        current_user = request.user

        current_user_object = OtherRequests.objects.filter(user=current_user).order_by('-id')
        


        return render(request, 'users/view_requests.html', {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'current_user_object': current_user_object})





@login_required(login_url='student_login')
def profile(request, u):
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        

        
        return render(request, 'users/profile.html', {'user_profile':user_profile, 'today':today, 'current_time': current_time})


@login_required(login_url='student_login')
def settings(request):

    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        

        if request.method == 'POST':
            if request.FILES.get('image') == None:
                user = request.user.username
                address = request.POST['address']
                contact = request.POST['contact']
                image = user_profile.profile_img

                user_profile.address = address
                user_profile.contact = contact
                user_profile.profile_img = image

                user_profile.save()

                messages.success(request, f"Information saved")

                return redirect('settings')
            

            
            else:
                user = request.user.username
                address = request.POST['address']
                contact = request.POST['contact']
                image = request.FILES.get('image')

                user_profile.user = request.user
                user_profile.address = address
                user_profile.contact = contact
                user_profile.profile_img = image

                user_profile.save()

                messages.success(request, f"Information saved")

                return redirect('settings')

        
        return render(request, "users/settings.html", {'user_profile':user_profile, 'today':today, 'current_time':current_time})



@login_required(login_url='student_login')
def delete_course(request):

    if request.method == 'POST':
        course = request.POST['delete_course']

        delete_course = Enrollment.objects.get(user=request.user, course_name = course)
        delete_course.delete()

        messages.warning(request, f"{course} dropped")

        return redirect("enrollment")
    
    return redirect("enrollment")

        



@login_required(login_url='student_login')
def fees(request):

    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        fees_object = Fees.objects.filter(user=request.user)


        if request.method == 'POST':

            fees_payment = Fees.objects.get(user=request.user)
            paid_fees = int(request.POST['payment'])
            

            fees_payment.paid = fees_payment.paid + paid_fees
            fees_payment.balance = fees_payment.balance - paid_fees

            fees_payment.save()

            messages.info(request, f"Thank you for your payment of {paid_fees}")

    




        return render(request, "users/fees.html" , {'user_profile':user_profile, 'today':today, 'current_time': current_time, 'fees_object': fees_object})



    
            

    return render(request, "users/online_class.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time,'class_time': class_time,})


@login_required(login_url='student_login')
def online_class(request):
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        class_time = "no"
        hour = int(now.strftime("%H"))


        if Enrollment.objects.filter(user=request.user):
            user_enrollments = Enrollment.objects.filter(user=request.user)
            for enrollment in user_enrollments:

                if enrollment.course_time == 'morning' and hour >8 and hour <12:
                    class_time = "yes"
                    shift_course = Enrollment.objects.get(course_time = 'morning', user=request.user)

                    return render(request, "users/online_class.html", {'user_profile': user_profile,
                        'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course': shift_course})




                elif enrollment.course_time == 'afternoon' and hour >11 and hour <15:
                    class_time = "yes"
                    shift_course = Enrollment.objects.get(course_time = 'afternoon', user=request.user)

                    return render(request, "users/online_class.html", {'user_profile': user_profile,
                        'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course': shift_course})




                elif enrollment.course_time == 'evening' and hour >14 and hour <18:
                    class_time = "yes"
                    shift_course = Enrollment.objects.get(course_time = 'evening', user=request.user)

                    return render(request, "users/online_class.html", {'user_profile': user_profile,
                        'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course': shift_course})




                elif enrollment.course_time == 'night' and hour >17 and hour <21:
                    class_time = 'Yes'
                    shift_course = Enrollment.objects.get(course_time = 'night', user=request.user)

                    return render(request, "users/online_class.html", {'user_profile': user_profile,
                        'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course': shift_course})


                    


            else:
                shift_course = "None of your enrolled courses have a class at this time"
                return render(request, "users/online_class.html", {'user_profile': user_profile,
                    'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course': shift_course})

    
        
        else:
            shift_course = "You are currently not enrolled in any courses"
            return render(request, "users/online_class.html", {'user_profile': user_profile,
            'today':today, 'current_time': current_time,'class_time': class_time, 'shift_course':shift_course})
        
    


@login_required(login_url='student_login')
def exam(request):
    
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        exam_time = "no"

        month = now.strftime("%m")

        if int(month) == 5 or int(month) == 11:
            exam_time = "yes"

                

        return render(request, "users/exam.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time,'exam_time': exam_time,})


@login_required(login_url='student_login')
def voting(request):
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        form = VoteForm()

        if UserVotes.objects.filter(voter=request.user):
            votes_object = UserVotes.objects.get(voter=request.user)

            votes_count = Voting.objects.all()

            option1_votes = Voting.objects.get(id=1)
            option1_votes = option1_votes.votes


            option2_votes = Voting.objects.get(id=2)
            option2_votes = option2_votes.votes

            option3_votes = Voting.objects.get(id=3)
            option3_votes = option3_votes.votes

            option4_votes = Voting.objects.get(id=4)
            option4_votes = option4_votes.votes

            option5_votes = Voting.objects.get(id=5)
            option5_votes = option5_votes.votes

            option6_votes = Voting.objects.get(id=6)
            option6_votes = option6_votes.votes

            option7_votes = Voting.objects.get(id=7)
            option7_votes = option7_votes.votes

            total_votes = option1_votes + option2_votes + option3_votes + option4_votes + option5_votes + option6_votes + option7_votes


            return render(request, "users/voting.html", {'user_profile': user_profile, 'today':today, 
            'current_time': current_time,'votes_object': votes_object, 'votes_count':votes_count, 'total_votes':total_votes
            })
        

        else:
            if request.method == 'POST':
                form = VoteForm(request.POST)
                if form.is_valid():
                    vote = form.cleaned_data['vote']
                    vote_instance = Voting.objects.get(option=vote)
                
                    votes_object = UserVotes.objects.create(voter=request.user, chosen_option = vote_instance, has_voted = True)

                    chosen_option = Voting.objects.get(option=vote)
                    chosen_option.votes = chosen_option.votes+1
                    chosen_option.save()

                    messages.info(request, f"voted {vote}")
                    


                    return redirect('voting')
        return render(request, "users/voting.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'form':form })


@login_required(login_url='student_login')
def enrollment(request):

    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        student_courses = Enrollment.objects.filter(user = request.user) 


        return render(request, "users/enrollment.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'student_courses':student_courses})

@login_required(login_url='student_login')
def add_course(request):
    user_profile = UserInfo.objects.get(user=request.user)
    if user_profile.is_teacher ==True:
        messages.warning(request, "You are logged in as a teacher and trying to access student's portal")
        return redirect('teacher_dashboard') 

    else:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        fees_object = Fees.objects.get(user=request.user)
        available_courses = AvailableCourses.objects.filter(course_for= user_profile.degree_title) | AvailableCourses.objects.filter(course_for = 'all') 
        shift =[]
        i = 0

        if Enrollment.objects.filter(user=request.user):
            enrollment_object = Enrollment.objects.filter(user=request.user)

            for courses in enrollment_object:
                
                shift.append(courses.course_time)
                available_courses = available_courses.exclude(course_time=shift[i])
                i= i+1
        
    
        if request.method == 'POST':

            if not request.POST:
                return redirect('add_course')
            course = request.POST['course']
            
            course = AvailableCourses.objects.get(course_name=course)

            add_course = Enrollment.objects.create(user=request.user, course_name=course.course_name, course_for=course.course_for, course_time=course.course_time)
            add_course.save()

            fees_object.course_fees = fees_object.course_fees + 10000
            fees_object.balance = fees_object.balance + 10000
            fees_object.save()

            messages.info(request, f"{course} course added ")

            return redirect('enrollment')
        
        return render(request, "users/add_course.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'available_courses':available_courses})






    