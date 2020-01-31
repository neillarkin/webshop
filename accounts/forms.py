from django import forms
from django.forms.widgets import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

"""User login form"""
class UserLoginForm(forms.Form):

    # special password textbox constructed from CharField class in Django Forms library
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'name@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput) 


"""Form used to register a new user. Constructed with Django UserCreationForm param"""
class UserRegistrationForm(UserCreationForm):
    
    #Labels are used for password as Django will use form field 'name' by default
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)
    
    
    #Inner class used to specify more information about the parent class
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    #Validate form fields using Django clean_data function with the 'self' object
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        # The filter function checks if the email already exists in the database
        # iexact() runs case-insensitive query on the database to check that...
        # ...the same username with a different case isn't already present
        if User.objects.filter(email__iexact=email).exclude(username__iexact=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        #Check if either field is blank
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        #Check if both fields passwords are equal
        if password1 != password2:
            raise ValidationError("Passwords must match")
        
        return password2