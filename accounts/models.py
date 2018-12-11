from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ## 1:Mail、2:Twitter、3:Facebook
    social_flag = models.IntegerField(default=1)
