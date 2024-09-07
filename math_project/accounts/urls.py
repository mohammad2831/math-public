from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns =[
   # path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('register_serializers/', views.UserRegisterView.as_view(), name='user_register'),
    path('login_serializers/', views.UserLoginView.as_view(), name='user_login'),
    path('profile_serializers/', views.UserProfileView.as_view(), name='user_profile'),
    path('verify_serializers/', views.UserRegisterVerifyCodeView.as_view(), name= 'user_register_verify_code'),




   
  #  path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'), 
]