from django.urls import path
from . import views
from .views import logout_view
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    # Add other auth-related URLs as needed
]