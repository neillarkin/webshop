from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

""" Test to verify the forms are validating correctly """
class TestUserLoginForm(TestCase):
    
    def test_login_form(self):
        form = UserLoginForm({'username': 'name', 'password': 'Pass_12345' })
        self.assertTrue(form.is_valid())
        
        
    def test_registration_form_is_valid(self):
        form = UserRegistrationForm({'email': 'name@example.com', 'username': 
            'name', 'password1': 'Pass_12345', 'password2': 'Pass_12345' })
        self.assertTrue(form.is_valid())
        
    def test_registration_form_not_valid(self):
        form = UserRegistrationForm({'email': 'name@example.com', 'username': 
            'name', 'password1': 'Pass_12345', 'password2': 'Pass_123456' })
        self.assertFalse(form.is_valid())