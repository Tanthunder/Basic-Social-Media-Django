from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as authviews

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('edit/', views.edit, name = 'edit'),
    path('', views.index, name = 'index'),
    path('logout/', authviews.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('password_change/',authviews.PasswordChangeView.as_view(template_name = 'users/password_change_form.html'), name = 'password_change'),
    path('password_change_done/',authviews.PasswordChangeDoneView.as_view(template_name = 'users/password_change_done.html'), name = 'password_change_done'),
    path('password_reset/',authviews.PasswordResetView.as_view(template_name = 'users/password_reset_form.html'), name = 'password_reset'),
    path('password_reset/done',authviews.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>',authviews.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',authviews.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'), name = 'password_reset_complete'),
]
