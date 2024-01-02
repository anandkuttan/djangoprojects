from django.shortcuts import render
from movie.models import Movie
from Film.forms import bookform
# Create your views here.

def home(request):
    return render(request,'home.html')


def viewfilm(request):
    b = Movie.objects.all()
    return render(request, 'viewfilm.html', {'film': b})


#
# def addfilm1(request):#builed in
#     form=bookform()
#     if(request.method=="POST"):
#         form=bookform(request.POST)
#         if(form.is_valid()):
#             form.save()
#             return viewfilm(request)

def viewfilmbyid(request,p):
    b=Movie.objects.get(id=p)
    return render(request, 'viewfilmbyid.html', {'film': b})


def deletefilmbyid(request,p):
    b = Movie.objects.get(id=p)
    b.delete()
    return viewfilm(request)


def editfilmbyid(request,p):
    b = Movie.objects.get(id=p)
    form = bookform(instance=b)
    if (request.method == "POST"):
        form = bookform(request.POST, request.FILES, instance=b)
        if (form.is_valid()):
            form.save()
            return viewfilm(request)
    return render(request, 'edit.html', {'form': form})