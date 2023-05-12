from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('post/<slug:slug>', views.post, name="post"),
    path('post/<slug:slug>/<str:pk>/', views.deleteComment, name="delete-comment"),
]