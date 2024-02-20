from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_dcmpatient = models.BooleanField(default=False)
    is_dcmdoctor = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    user_type = models.CharField(max_length=50, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_custom_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_custom_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class DcmPatient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
    	return self.user.username


class DcmDoctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)


    def __str__(self):
    	return self.user.username


    

