from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>', views.profile_detail, name='profile_detail'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
