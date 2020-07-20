from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signUp,name='signup'),
    path('adminlogin',views.recLogin,name='adminLogin'),
    path('analysis',views.listResume,name="Scan"),
    path('upload',views.uploadResume,name="UploadResume"),
    path('signupsuccess',views.signuptoLogin,name="successreg"),
    path('uploadsuccess',views.thanksUploadResume,name="successupload"),
    path('scanned',views.filteredResult,name="scanSuccess")
]