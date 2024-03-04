from django.contrib.auth.models import User
from django.db import models



# Create your models here.

gender_choices = {
    "MS": "masculino",
    "FM": "feminino",
    "OT": "outro",
}


class user_profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profile_images")
    bio = models.TextField(max_length=240)
    gender = models.CharField(choices=gender_choices, max_length=10)
    nickname = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nickname} - {self.name}"
    

