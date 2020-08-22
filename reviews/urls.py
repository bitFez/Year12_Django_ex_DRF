from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:review_id>/', views.filmreview, name='filmreview'),
    path('register/', views.registration, name='register'),
    path('submitreview/', views.submitreview, name='submitreview'),
]
