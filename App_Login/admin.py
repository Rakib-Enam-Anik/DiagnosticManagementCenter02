from django.contrib import admin
from App_Login.models import UserProfile, DcmDoctor, DcmPatient

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(DcmPatient)
admin.site.register(DcmDoctor)
