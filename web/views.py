from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from django.contrib.auth import logout
from .forms import Profileupdateform, Blogpost
from . models import Contact, Blog

# Create your views here.
def index(request):
    c_post = Blog.objects.order_by('-pubdate')
    return render(request, 'index.html', {'c_post': c_post})

def login(request):
    if request.method == 'POST':
        eml = request.POST['eml']
        pas = request.POST['pas']
        user = auth.authenticate(username=eml, password=pas)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 = request.POST['psw-repeat']
        if psw == psw2:
            if User.objects.filter(username=email).exists():
                messages.info(request, 'Email already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, password=psw, first_name=name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        cont = Contact(name=name, email=email, mobile=phone, msg=msg)
        cont.save()
        messages.success(request, 'Your Message has been sent!')
        return redirect('contact')
    return render(request, 'contact.html')

def logoutuser(request):
    logout(request)
    return redirect('index')


def profile(request):
    if request.method == 'POST':
        p_form = Profileupdateform(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated')
            return redirect('profile')
    else:
        p_form = Profileupdateform(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }

    return render(request, 'profile.html', context)

def post(request):
    if request.method == 'POST':
        b_form = Blogpost(request.POST, request.FILES)
        if b_form.is_valid():
            obj = b_form.save(commit=False)
            obj.author = request.user
            obj.save()
            messages.success(request, 'You have successfully created a Blog')
            return redirect('index')
    else:
        b_form = Blogpost()
    return render(request, 'post.html', {'b_form': b_form})

def my_post(request, id):
    m_post = Blog.objects.get(id=id)
    return render(request, 'my_post.html', {'m_post': m_post})

def post_remove(request, id):
    d_post = Blog.objects.get(id=id)
    if request.user == d_post.author:
        messages.success(request, 'You have successfully deleted your post.')
        d_post.delete()
    else:
        messages.error(request, 'You are not authorized to delete this post . This post does not belong to you')
    return render(request, 'post_remove.html')
