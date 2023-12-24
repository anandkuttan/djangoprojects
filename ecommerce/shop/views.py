from django.shortcuts import render,redirect
from shop.models import category,product
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

def allcategories(request):
    c=category.objects.all()
    return render(request,'categories.html',{'c':c})


def allproducts(request,p):
    c=category.objects.get(name=p)
    p=product.objects.filter(category=c)
    return render(request, 'product.html', {'c':c,'p':p})

def detail(request,p):
    n=product.objects.get(name=p)

    return render(request,'detail.html',{'p':n})


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']

        if(p==cp):
            u=User.objects.create_user(username=u,password=p,email=e)
            u.save()
            return redirect('shop:allcate')
        else:
            return HttpResponse("password not matching")

    return render(request,template_name= 'register.html')

def user_login(request):
    if(request.method=="POST"):
        name=request.POST['u']
        pass1=request.POST['p']
        user=authenticate(username=name,password=pass1)
        if user:
            login(request,user)
            return redirect('shop:allcate')
        else:
            messages.error(request,"invalid credentails")


    return render(request,template_name= 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)