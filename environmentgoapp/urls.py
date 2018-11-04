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
from django.urls import path, reverse_lazy
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, auth_logout
from django_registration.backends.one_step.views import RegistrationView


from environmentgo import views


urlpatterns = [
    path('accounts/register/', RegistrationView.as_view(
        template_name='registration/registration_form.html',
        extra_context={'title': 'Register'},
        success_url=reverse_lazy('home'),
    ), name='registration_register'),
    path('accounts/login/', LoginView.as_view(
        template_name='registration/login.html',
        extra_context={'title': 'Login'},
    ), name='auth_login'),
    url(r'^logout/$', auth_logout, {'next_page': '/'}, name='auth_logout'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', views.map_image_data, name='home'),
    path('upload', views.model_form_upload, name='add_image'),
    path('create', views.map_image_data, name='map_page'),
    path('images/<int:id>', views.download, name='image_view')
]