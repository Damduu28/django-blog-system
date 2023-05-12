from django import forms

from blog.models import Post
from users.models import User

class PostCreateForm(forms.ModelForm):
    publish = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    class Meta:
        model = Post
        fields = ['title', 'description', 'publish']
    
class ProfileUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio', 'avatar']
        