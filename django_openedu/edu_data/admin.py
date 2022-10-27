from django.contrib import admin

# Register your models here.
# These models are registered to be able to see and edit them in the admin website

from .models import EduMaterial
admin.site.register(EduMaterial)
