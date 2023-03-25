from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import UserRegistartionForm, VoteForm
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime
from django.contrib.auth import authenticate, login
from .models import OtherRequests, UserInfo, AvailableCourses, Enrollment, Fees, Voting, Votes
from django.db.models import Q
from django.contrib.auth.models import User
import random


# Create your views here.

def register(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    form = UserRegistartionForm()
    if request.method == 'POST':
        form = UserRegistartionForm(request.POST)  

        if form.is_valid():
            username = form.cleaned_data.get('username')


            new_user = form.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            degree_title = ['bscs', 'bba', 'bms', 'bfd']

            student_degree_title = random.choice(degree_title)





            new_profile = UserInfo.objects.create(user=username, degree_title=student_degree_title)
            new_profile.save()


            user_model = User.objects.get(username=username)
            new_enrollment = Enrollment.objects.create(user=user_model)
            new_enrollment.save()

            new_user_fees = Fees.objects.create(user=user_model, enrollment_fees=5000, monthly_fees = 2000, balance=7000)
            new_user_fees.save()
            
            messages.success(request, f"Account created for {username}")

            return redirect('dashboard')
        
        else:
            form = UserRegistartionForm()
            messages.warning(request, f'Please enter the correct information')
        return render(request, 'users/register.html', {'form': form })
    
    return render(request, 'users/register.html', {'form': form })

@login_required(login_url='index')
def dashboard(request):

    today = date.today()
    now = datetime.now()

    user_profile = UserInfo.objects.get(user=request.user)

    fees_object = Fees.objects.get(user=request.user)

    current_time = now.strftime("%H:%M:%S")
    
    return render(request, 'users/dashboard.html', {'today':today, 'current_time': current_time, 
    'user_profile':user_profile, 'fees_object':fees_object})

@login_required(login_url='index')
def request(request):

    user_profile = UserInfo.objects.get(user=request.user)
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


@login_required(login_url='index')
def view_requests(request):

    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    request_object = OtherRequests.objects.all()

    current_user = request.user

    current_user_object = OtherRequests.objects.filter(user=current_user)
    


    return render(request, 'users/view_requests.html', {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'current_user_object': current_user_object})





@login_required(login_url='signin')
def profile(request, u):
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    

    
    return render(request, 'users/profile.html', {'user_profile':user_profile, 'today':today, 'current_time': current_time})


@login_required(login_url='signin')
def settings(request):

    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            user = request.user.username
            address = request.POST['address']
            contact = request.POST['contact']
            image = user_profile.profile_img

            user_profile.user = user
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

            user_profile.user = user
            user_profile.address = address
            user_profile.contact = contact
            user_profile.profile_img = image

            user_profile.save()

            messages.success(request, f"Information saved")

            return redirect('settings')

    
    return render(request, "users/settings.html", {'user_profile':user_profile, 'today':today, 'current_time':current_time})



@login_required(login_url='signin')
def add_courses(request):
    user_profile = UserInfo.objects.get(user=request.user)
    fees = Fees.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


    
    available_courses = AvailableCourses.objects.filter(course_for=user_profile.degree_title) | AvailableCourses.objects.filter(course_for ='all')



    if request.method == 'POST':
        course = request.POST['course']

        add_course = Enrollment.objects.get(user = request.user)

        if course == add_course.course1 or course == add_course.course2 or course == add_course.course3 or course == add_course.course4 or course == add_course.course5 or course == add_course.course6:
            messages.warning(request, f"You are already enrolled in the selected course, please choose another course")
            return redirect('enrollment')

        if add_course.course1 == "":
            add_course.course1 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()

        elif add_course.course2 == "":
            add_course.course2 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()

        elif add_course.course3 == "":
            add_course.course3 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()

        elif add_course.course4 == "":
            add_course.course4 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()

        elif add_course.course5 == "":
            add_course.course5 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()

        elif add_course.course6 == "":
            add_course.course6 = course

            add_course.save()

            fees.course_fees = fees.course_fees + 10000
            fees.balance = fees.balance + 10000
            fees.save()


        else:
            messages.warning(request, f"Your slots are already full, can't add any more")
            return redirect('enrollment')


        messages.success(request, f"{course} added, see enrollment")
    return render(request, "users/add_courses.html", {'user_profile':user_profile, 'today':today, 'current_time': current_time, 'available_courses' :available_courses})


@login_required(login_url='signin')
def enrollment(request):

    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


    courses = Enrollment.objects.filter(user= request.user)



    
    return render(request, "users/enrollment.html", {'user_profile':user_profile, 'today':today, 'current_time': current_time, 'courses': courses})


@login_required(login_url='signin')
def delete_course(request):

    if request.method == 'POST':
        course = request.POST['delete_course']


        enrolled_courses = Enrollment.objects.get(user=request.user)

        if enrolled_courses.course1 == course: 
            enrolled_courses.course1 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")

        elif enrolled_courses.course2 == course: 
            enrolled_courses.course2 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")

        elif enrolled_courses.course3 == course: 
            enrolled_courses.course3 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")

        elif enrolled_courses.course4 == course: 
            enrolled_courses.course4 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")

        elif enrolled_courses.course5 == course: 
            enrolled_courses.course5 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")

        elif enrolled_courses.course6 == course: 
            enrolled_courses.course6 = "Course Dropped"
            enrolled_courses.save()
            messages.success(request, "course dropped")
            

        return redirect("enrollment")
        

    else:

        return redirect("enrollment")



@login_required(login_url='signin')
def fees(request):

    user_profile = UserInfo.objects.get(user=request.user)
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


@login_required(login_url='signin')
def online_class(request):
    
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    class_time = "no"

    hour = now.strftime("%H")
 
    


    
    for i in range(9,22):
        if int(hour) == i:
            class_time = "yes"
    
            

    return render(request, "users/online_class.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time,'class_time': class_time,})



@login_required(login_url='signin')
def exam(request):
    
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    exam_time = "no"

    month = now.strftime("%m")

    if int(month) == 5 or int(month) == 11:
        exam_time = "yes"

            

    return render(request, "users/exam.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time,'exam_time': exam_time,})


@login_required(login_url='signin')
def voting(request):
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    form = VoteForm()

    
    if Votes.objects.filter(voter=request.user):
        votes_object = Votes.objects.get(voter=request.user)

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
            
                votes_object = Votes.objects.create(voter=request.user, option = vote, has_voted = True)

                chosen_option = Voting.objects.get(option=vote)
                chosen_option.votes = chosen_option.votes+1
                chosen_option.save()

                messages.info(request, f"voted {vote}")
                


                return redirect('voting')
    return render(request, "users/voting.html", {'user_profile': user_profile, 'today':today, 'current_time': current_time, 'form':form })


