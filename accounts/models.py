from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ## ハンドルネーム
    name = models.CharField(max_length=50, blank=True)

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
    profile_content = models.TextField(validators=[MaxLengthValidator(200)], blank=True)

    ## Twitter
    twitter = models.CharField(max_length=50, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def __str__(self):
        return self.name
