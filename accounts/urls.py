from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
#     path('logout', views.logout, name='logout'),
#     path('register', views.register, name='register'),
#     path('profile', views.view_profile, name='view_profile'),
#     path('profile_edit', views.edit_profile, name='edit_profile'),
#     path('change_password', views.change_password, name='change_password'),
]
