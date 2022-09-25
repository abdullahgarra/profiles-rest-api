from django.contrib import admin

from profiles_api import models

#register user profile model with the admin site
admin.site.register(models.UserProfile)
