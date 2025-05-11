from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='signup'),
    path('login/', views.signin.as_view(), name='signin'),
    path('logout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile')
]