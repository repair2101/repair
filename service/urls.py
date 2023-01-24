"""service URL Configuration

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
from django.urls import path, include
from crud import views
from rest_framework import routers
from django.contrib.auth import views as auth_views 


router_employee = routers.SimpleRouter()
router_employee.register(r'employee', views.EmployeeViewSet)

router_request = routers.SimpleRouter()
router_request.register(r'request', views.RequestViewSet)

router_stage = routers.SimpleRouter()
router_stage.register(r'stage', views.StageViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index, name='index'),
    
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/', include(router_employee.urls)),     #http://127.0.0.1:8000/api/employee/, 
    path('api/', include(router_request.urls)),     #http://127.0.0.1:8000/api/request/, 
    path('api/', include(router_stage.urls)),     #http://127.0.0.1:8000/api/stage/, 
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('settings/account/$', views.UserUpdateView.as_view(), name='my_account'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),


]
