"""
URL configuration for restapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from restapp import views
from restapp.views import Studentlist, Studentadd,Taskadd,Tasklist,Statusupdate,gettaskbylogin,gettasklistbylogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listusers',views.list_users),
    path('getuser/<int:userid>',views.get_user),
    path('adduser',views.add_user),
    path('addbook',views.add_book),
    path('update/<int:userid>',views.userupdate),
    path('edit/<int:userid>',views.useredit),
    path('updatebook/<int:id>',views.bookupdate),
    path('editbook/<int:id>',views.bookedit),
    path('delete/<int:userid>',views.delete_user),
    path('deletebook/<int:id>',views.delete_user),
    path('getbook/<int:id>',views.get_book),
    path('login',views.login_user),
    path('logout',views.logout_user),
                                        
    path('liststudent',Studentlist.as_view()),                                   
    path('addstudent',Studentadd.as_view()),
    
    path('gettask/<int:taskid>',views.gettask),
    path('addtask',Taskadd.as_view()),
    path('listtask',Tasklist.as_view()),
    path('statusupdate/<int:taskid>',Statusupdate.as_view()),
    path('gettaskby',gettaskbylogin.as_view()),
    path('gettasklistby',gettasklistbylogin.as_view()),
    
]
