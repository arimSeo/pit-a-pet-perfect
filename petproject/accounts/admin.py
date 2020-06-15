from django.contrib import admin
from .models import RegiProfile, PlusPhoto, UserLocation, Address

admin.site.register(RegiProfile)
# Register your models here.
admin.site.register(PlusPhoto)
admin.site.register(Address)
