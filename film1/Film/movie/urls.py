"""
URL configuration for Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from movie import views
app_name='movie'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('viewfilm/',views.viewfilm,name="viewfilm"),
    path('viewfilmbyid/<int:p>',views.viewfilmbyid,name="viewfilmbyid"),
path('deletefilmbyid/<int:p>',views.deletefilmbyid,name="deletefilmbyid"),
path('editfilmbyid/<int:p>',views.editfilmbyid,name="editfilmbyid"),
    # path('addfilm1/',views.addfilm1,name="addfilm1"),



]


