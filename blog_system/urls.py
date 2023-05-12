from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views
from profiles.views import (createPost, 
                            updateProfile,
                            updatePost,
                            deletePost
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('create-post/', createPost, name="create-post"),
    path('update-post/<str:pk>/', updatePost, name="update-post"),
    path('delete-post/<str:pk>/', deletePost, name="delete-post"),
    path('update-profile/<str:pk>/', updateProfile, name="update-profile"),
    path('user-profile/', include('profiles.urls')),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)