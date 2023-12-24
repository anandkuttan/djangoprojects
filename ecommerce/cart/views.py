
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from shop.models import product
from cart.models import cart
from cart.models import Account,Order


def cartview(request):
    total=0
    u=request.user
    try:
        car=cart.objects.filter(user=u)

        for i in car:
            total+=i.quantity*i.product.price
    except:
        pass
    return render(request,'cart.html',{'c':car,'total':total})


@login_required
def add_to_cart(request,p):
    pro=product.objects.get(name=p)
    u=request.user
    try:
        car=cart.objects.get(user=u,product=pro)
        if(car.quantity<car.product.stock):
            car.quantity+=1
        car.save()
    except:
        car=cart.objects.create(user=u,product=pro,quantity=1)
        car.save()


    return redirect('cart:cartview')


def minus(request,p):
    p=product.objects.get(name=p)
    u=request.user
    try:
        car=cart.objects.get(user=u,product=p)
        if(car.quantity>1):
            car.quantity-=1
        car.save()
    except:
        pass
    return redirect('cart:cartview')

def delete(request,p):
    p=product.objects.get(name=p)
    u=request.user
    try:
        car=cart.objects.get(user=u,product=p)
        car.delete()
    except:
        pass
    return redirect('cart:cartview')


def orderform(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        u=request.user
        car=cart.objects.filter(user=u)
        total=0
        for i in car:
            total+=i.quantity*i.product.price

        ac=Account.objects.get(acctnum=n)
        if(ac.amount>=total):
            ac.amount=ac.amount-total
            ac.save()

            for i in car:
                o=Order.objects.create(user=u,product=i.product,address=a,phone=p,no_of_items=i.quantity,order_status="paid")
                o.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            car.delete()
            msg="Order placed successfully"
            return render(request,'orderdetail.html',{'m':msg})




        else:
            msg="insufficient amount in user account.you cannot place order."
            return render(request, 'orderdetail.html', {'m': msg})




    return render(request, 'orderform.html')




def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request, 'orderview.html',{'o':o})



