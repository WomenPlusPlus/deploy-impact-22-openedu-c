from django.contrib import admin

# Register your models here.
# These models are registered to be able to see and edit them in the admin website

from .models import EduMaterial, Author, Publisher, Institution, Media_Channel
admin.site.register(EduMaterial)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Institution)
admin.site.register(Media_Channel)

