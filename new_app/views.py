from django.contrib import messages
from rest_framework import status
from rest_framework.response import Response

from new_app.forms import PublisherForm, CustomerForm, RegistrationForm, BlogForm
from new_app.models import Publisher, Customer, blog

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm




def new(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'admin.html')

def publishers(request):
    return render(request, 'publisher.html')

def customers(request):
    return render(request, 'customer.html')



def login_view(request):
    return render(request, 'login.html')





def publisher_register(request):
    pub_form = PublisherForm()
    reg_form = RegistrationForm()



    if request.method == 'POST':
        pub_form = PublisherForm(request.POST, request.FILES)
        reg_form = RegistrationForm(request.POST)
        if pub_form.is_valid() and reg_form.is_valid():
            reg1 =reg_form.save(commit=False)
            reg1.is_student = True
            reg1.save()
            stud1 = pub_form.save(commit=False)
            stud1.user = reg1
            stud1.save()
            return redirect('login1')
        # Render the form with errors if it's not valid

    return render(request, "register.html", {"reg_form": reg_form, "pub_form": pub_form})

def customer_register(request):
    cus_form = CustomerForm()
    reg_form = RegistrationForm()



    if request.method == 'POST':
        cus_form = CustomerForm(request.POST, request.FILES)
        reg_form = RegistrationForm(request.POST)
        if cus_form.is_valid() and reg_form.is_valid():
            reg1 =reg_form.save(commit=False)
            reg1.is_parent = True
            reg1.save()
            parent1 = cus_form.save(commit=False)
            parent1.user = reg1
            parent1.save()
        # Render the form with errors if it's not valid

    return render(request, "register2.html", {"reg_form": reg_form, "cus_form": cus_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #username is same as in the login.html page
        print(username)
        password = request.POST.get('pass') #pass is same in the login.html page
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('base') #base is the path name redirect to admin page
            elif user.is_publisher:
                return redirect('student') #student is the path name redirect to admin page
            elif user.is_customer:
                return redirect('parent') #parent is the path name redirect to admin page
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'view_publisher.html')

def view(request):
    data =  Publisher.objects.all()
    return render(request, "view_publisher.html", {"data": data})

def view1(request):
    data =  Customer.objects.all()
    return render(request, "view_customer.html", {"data": data})


def delete(request,id):
    if request.method == 'POST':

        delt1 = Publisher.objects.get(id=id)
        reg_details= delt1.user
        delt1.delete()
        reg_details.delete()

        return redirect("view")
    return render(request,"admin.html")

def delete1(request,id):
    if request.method == 'POST':

        delt1 = blog.objects.get(id=id)

        delt1.delete()
        

        return redirect("view2")
    return render(request,"admin.html")

def update(request,id):
    pub_data = Publisher.objects.get(id=id)
    pub_reg_form = PublisherForm(instance=pub_data)

    if request.method == 'POST':
        pub_reg_form1 = PublisherForm(request.POST,request.FILES,instance=pub_data)
        if pub_reg_form1.is_valid():
            pub_reg_form1.save()
            return redirect("view")

    return render(request,'update.html',{'stud_form':pub_reg_form})

def blog_register(request):
    blog_form = BlogForm()



    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)

        if blog_form.is_valid():

            food1 = blog_form.save(commit=False)
            food1.save()
            return redirect('view2')
        # Render the form with errors if it's not valid

    return render(request, "registerBlog.html", { "blog_form": blog_form})


def view2(request):
    data =  blog.objects.all().order_by("id").values()
    return render(request, "view_bloglist.html", {"data": data})

def blogupdate(request,id):
    blog_data = blog.objects.get(id=id)
    blog_reg_form = BlogForm(instance=blog_data)

    if request.method == 'POST':
        food_reg_form1 = BlogForm(request.POST,request.FILES,instance=blog_data)
        if food_reg_form1.is_valid():
            food_reg_form1.save()
            return redirect("view2")

    return render(request,'blog_update.html',{'blog_form':blog_reg_form})

def view_blog_user(request):
    data = blog.objects.all()
    return render(request,"view_bloglist_student.html",{"data": data})


#api_view


