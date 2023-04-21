from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import UserInfo
from datetime import date
from datetime import datetime
from .models import Post, PostLikes, Comments
from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url='/')
def make_post(request):
    user_type = UserInfo.objects.get(user=request.user)
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        new_post = Post.objects.create(user=request.user, title=title, post=content)
        new_post.save()

        if user_type.is_student==True:
            return redirect('dashboard')
        else:
            return redirect('teacher_dashboard')
        
   
    
    else:
        if user_type.is_student==True:
            return render(request, "posts/users_make_post.html", {'user_type':user_type, 'user_profile':user_profile ,
                        'today':today, 'current_time': current_time,})
        else:
            return render(request, "posts/make_post.html", {'user_type':user_type})




@login_required(login_url='/')
def post_like(request):
    post_id = request.GET.get('post_id')
    post_object = Post.objects.get(id=post_id)
    user_type = UserInfo.objects.get(user=request.user)
    if PostLikes.objects.filter(user=request.user, post_id=post_id):
        like_object = PostLikes.objects.get(user=request.user, post_id=post_id)
        like_object.delete()

        post_object.number_of_likes= post_object.number_of_likes-1
        post_object.save()

        if user_type.is_student==True:
            return redirect('dashboard')
        else:
            return redirect('teacher_dashboard')
            

            

    else:
        like_object = PostLikes.objects.create(user = request.user, post_id=post_id)
        like_object.save()

        post_object.number_of_likes= post_object.number_of_likes+1
        post_object.save()
        if user_type.is_student==True:
            return redirect('dashboard')
        else:
            return redirect('teacher_dashboard')
    


@login_required(login_url='/')
def my_posts(request, u):
    user_type = UserInfo.objects.get(user=request.user)
    user_profile = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    likes = PostLikes.objects.filter(user=request.user)
    comments = Comments.objects.all()


    p = Paginator(Post.objects.filter(user=u).order_by('-id'), 6)
    page = request.GET.get('page')
    user_posts = p.get_page(page)


    if user_type.is_student == True:
        return render(request,"posts/my_posts.html",{'user_profile':user_profile, 'today':today,
                    'current_time': current_time, 'user_posts': user_posts, 'likes':likes, 'comments':comments, })

    else:
        return render(request,"posts/teacher_posts.html", {'user_type':user_type,
                    'likes':likes, 'user_posts':user_posts,'comments':comments,})

@login_required(login_url='/')
def comment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        post_id = request.POST['post_id']

        save_comment = Comments.objects.create(user=request.user, post_id=post_id, comment=comment)

        return redirect('/')




@login_required(login_url='/')
def delete_post(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']

        delete_post = Post.objects.get(id=post_id)
        delete_post.delete()
        

        return redirect('/')


@login_required(login_url='/')
def delete_comment(request):
    if request.method == 'POST':
        comment_id = request.POST['comment_id']

        delete_comment = Comments.objects.get(id=comment_id)
        delete_comment.delete()
        

        return redirect('/')

@login_required(login_url='/')
def edit_post(request, u):
    user_profile = UserInfo.objects.get(user=request.user)
    user_type = UserInfo.objects.get(user=request.user)
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    post = Post.objects.get(id=u)

    if post.user == request.user:


        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']

            post.title = title
            post.post = content
            post.save()

            return redirect('/')
        else:
            if user_type.is_student == True:
                return render(request, "posts/edit_post.html", {'user_profile':user_profile, 'today':today,
                'current_time': current_time, 'post':post,})

            else:
                return render(request, "posts/teacher_edit_post.html", {'user_type':user_type, 'post':post,})
            
    else:
        return redirect('/')


 
    


@login_required(login_url='/')
def edit_comment(request):
    if request.method == 'POST':
        comment_id = request.POST['comment_id']
        comment = request.POST['comment']
        
        edit_comment = Comments.objects.get(id=comment_id)
        edit_comment.comment = comment
        edit_comment.save()


        return redirect('/')



