from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.userProfile, name="user-profile"),
    path('<str:pk>/<str:post_id>/', views.publishPost, name="publish-post"),
    
]