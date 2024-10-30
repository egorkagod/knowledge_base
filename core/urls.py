from django.urls import path
import core.views as views
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
]
