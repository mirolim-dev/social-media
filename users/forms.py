from django.forms import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'age', 'country']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'bg-gray-200 mb-2 shadow-none  dark:bg-gray-800'