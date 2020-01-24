from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Wishlist(models.Model):
    artist_name = models.CharField(max_length=254, default='')
    record_name = models.CharField(max_length=254, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)  
    
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
  
    # def get_user(request):
    #     current_user = request.user
    #     return current_user
        
    # user = models.ForeignKey(current_user, on_delete=models.CASCADE,null=False)
 
    # def get_user(self, user_id):
    # #     try:
    # #         user = User.objects.get(pk=user_id)
    # #         if user.is_active:
    # #             return user
    # #         return None
    # #     except User.DoesNotExist:
    # #         return None
    
    
    
    def __str__(self):
         return self.artist_name