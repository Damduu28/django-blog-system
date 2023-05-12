from django.db import models
from django.contrib.auth.models import AbstractUser

from uuid import uuid4
import os

# Create your models here.
def avatar_upload_path(instanse, filename):
    upload_to = "profiles"
    ext = filename.split('.')[1]
    
    if instanse.pk:
        filename = "{}.{}".format(instanse.pk, ext)
    else:
        filename = "{}.{}".format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=254)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_path, default="avatar.png", null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        if not self.name:
            uname = self.username
        else:
            uname = self.name
        return uname
    
    @property
    def get_user_name(self):
        if not self.name:
            uname = self.username
        else:
            uname = self.name
        return uname
    
    @property
    def get_avatar_url(self):
        return self.avatar.url
    
    
