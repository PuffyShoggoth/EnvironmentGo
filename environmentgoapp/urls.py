"""environmentgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView
from django.urls import path, include, re_path
from django_registration.views import RegistrationView

from environmentgo import views

register_patterns = [
    path('register/', RegistrationView.as_view(
        template_name='registration/registration_form.html',
        extra_context={'title': 'Register'},
    ), name='registration_register'),
    path('login/', LoginView.as_view(
        template_name='registration/login.html',
        extra_context={'title': 'Login'},
    ), name='auth_login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='auth_logout'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password/reset/', PasswordResetView.as_view(), name='auth_password_reset'),
    re_path('^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(register_patterns)),
    path('', views.map_image_data, name='home'),
    path('upload', views.model_form_upload, name='add_image'),
    path('create', views.map_image_data, name='map_page'),
]
