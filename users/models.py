from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null =True, blank = True)
    photo = models.ImageField(null =True, blank = True,upload_to ='users/%Y/%m/%d')
    

    def __str__(self):
        return str(self.user)