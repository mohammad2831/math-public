from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=200, unique=False)
    is_active =models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_img = models.ImageField(null=True)
    profile_img_base64 = models.TextField(blank=True, null=True,)

    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['phone_number', 'full_name']

    def __str__(self):
        return self.email
    
    def has_perm(self , perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

class OtpCode(models.Model):
    phone_number=models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
