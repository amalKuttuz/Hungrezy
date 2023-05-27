from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to=None)
    phone_no=models.IntegerField()

