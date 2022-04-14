
   
from django.urls import path, include
from knox import views as knox_views
from . import views


urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', views.Register.as_view() , name='register'),
    path('api/auth/login', views.Login.as_view(), name='login'),
    path('api/auth/user', views.UserAPI.as_view(), name='user'),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]

