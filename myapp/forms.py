from django import forms
from .models import UserBlogs

class UserBlogsForm(forms.ModelForm):
    class Meta:
        model = UserBlogs
        fields = ['Title','BlogImages','BlogContent', 'author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['BlogImages'].widget.attrs.update({'accept': 'image/*'})