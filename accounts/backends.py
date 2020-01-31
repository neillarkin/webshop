from django.contrib.auth.models import User

"""Authenticate a user by an exact match on the email and password"""
""" Used by the Django authentiation system to retrieve a user instance"""
class CaseInsensitiveAuth:
    def authenticate(self, username=None, password=None):
       
    #Get instance of user by using the email address
        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user

            return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user

            return None
        except User.DoesNotExist:
            return None
