# from .models import User
from .models import UserProfile
from django.contrib import admin

# # @admin.register(User)
# class Users(admin.ModelAdmin):
#     pass
@admin.register(UserProfile)
class Person(admin.ModelAdmin):
    pass


