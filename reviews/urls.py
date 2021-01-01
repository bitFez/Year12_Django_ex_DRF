from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:review_id>/', views.filmreview, name='filmreview'),
    path('register/', views.registration, name='register'),
    path('submitreview/', views.submitreview, name='submitreview'),

    # DRF URL Patterns
    path('api-list/', views.ReviewsList.as_view()),
    path('api/<int:pk>/', views.ReviewsDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)