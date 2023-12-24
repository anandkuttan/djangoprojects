from django.shortcuts import render

from django.db.models import Q
from shop.models import product


def search(request):
    q=""
    pro=None
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
            pro=product.objects.filter(Q(name__icontains=q)|Q(desc__icontains=q))

    return render(request,'search.html',{'p':pro,'query':q})