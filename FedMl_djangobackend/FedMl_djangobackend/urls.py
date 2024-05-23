"""FedMl_djangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create_project/', views.create_project, name='create_project'),
    path('create_model/', views.create_model, name='create_model'),
    path('upload_train_data/', views.upload_train_data, name='upload_train_data'),
    path('upload_predict_data/', views.upload_predict_data, name='upload_predict_data'),
    path('start_predict/', views.start_predict, name='start_predict'),
    path('start_training/', views.start_training, name='start_training'),
    path('get_project_list/', views.get_project_list, name='get_project_list'),
]
