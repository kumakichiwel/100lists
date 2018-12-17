from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MaxLengthValidator

from django.contrib.auth.models import User

class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ## ハンドルネーム
    name = models.CharField(max_length=50)

    ## 1:Mailaddress、2:Twitter、3:Facebook
    social_flag = models.IntegerField(default=1)

    ## イメージ画像
    profile_image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/',
        blank=True
    )
    
    profile_image_edit = ImageSpecField(
        source='profile_image',
        processors=[ResizeToFill(150, 150)],
        format='JPEG'
    )

    ## プロフィール説明
    profile_content = models.TextField(validators=[MaxLengthValidator(200)])

    def __str__(self):
        return self.name
