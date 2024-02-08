from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'password', 'password2', 'email']
        
# class RegisterForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']

#     def clean_password2(self):
#         # Check if the two password entries match
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')

#         if password and password2 and password != password2:
#             raise forms.ValidationError('Passwords do not match')

#         return password