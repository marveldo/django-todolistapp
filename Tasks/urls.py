from django.urls import path,include
from . import views


urlpatterns = [
    path('home/', views.home, name= 'home'),
    path('',views.loginuser, name= 'login'),
    path('register/', views.registerUser, name = 'register'),
    path('createtask/', views.Createtask, name ='create'),
    path('Edit/<str:pk>/', views.Edittask, name = 'edit' ),
    path('delete/', views.deleteprojects, name = 'delete'),
    path('logout/', views.logoutuser, name = 'logout')
]