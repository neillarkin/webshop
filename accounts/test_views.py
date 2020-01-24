from django.test import TestCase
from django.shortcuts import get_object_or_404
from accounts.forms import UserLoginForm, UserRegistrationForm

class TestAccountViews(TestCase):  
    
    def test_get_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")
       