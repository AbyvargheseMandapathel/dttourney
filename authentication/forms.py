from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from ads.models import Author

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm

class UserRegistrationForm(UserCreationForm):
    # Styling the username form fields
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'block w-full pr-10 border-red-300 text-red-900 placeholder-red-300 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm rounded-md',  
        'name': 'username', 
        'placeholder': 'Username'
    }))

    # Styling the password1 form fields
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'block w-full pr-10 border-red-300 text-red-900 placeholder-red-300 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm rounded-md',  
        'name': 'password1', 
        'placeholder': 'Password'
    }))

    # Styling the password2 form fields
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'block w-full pr-10 border-red-300 text-red-900 placeholder-red-300 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm rounded-md',  
        'name': 'password2', 
        'placeholder': 'Retype Password'
    }))
    
    # Making the email field required 
    email = forms.EmailField(required=True)

    # Styling the email form fields
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': ' content-center block w-full pr-10 border-red-300 text-red-900 placeholder-red-300 focus:outline-none focus:ring-red-500 focus:border-red-500 sm:text-sm rounded-md',  
        'placeholder': 'Email Address'
    }))


    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    def clean_email(self):
        email = self.cleaned_data['email']
        duplicate_email = User.objects.filter(email=email).exists()
        print("Email Taken")
        if duplicate_email:
            raise forms.ValidationError("This Email address is already in use.")
        return email


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': '',  
        'placeholder': 'Email Address'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")

        return email

class EmailSetPassword(SetPasswordForm):
    # Styling the password1 form fields
    new_password1 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',  
        'name': 'new_password1', 
        'placeholder': 'Password'
    }))

    # Styling the password2 form fields
    new_password2 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',  
        'name': 'new_password2', 
        'placeholder': 'Retype Password'
    }))

# Updating the User registration form
class UserUpdateForm(ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',  
        'name': 'first_name', 
        'placeholder': 'First Name'
    }))

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',  
        'name': 'last_name', 
        'placeholder': 'Last Name'
    }))

    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',  
        'placeholder': 'Email Address'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # exclude = ['user']

# Updating the profile form
class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['profile_pic']