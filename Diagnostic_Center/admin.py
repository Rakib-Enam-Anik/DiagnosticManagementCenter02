from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Technician)
admin.site.register(Nurse)
admin.site.register(Appointment)