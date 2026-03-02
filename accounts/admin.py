from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import Profile

class ProfileInLine(admin.StackedInLine):
    model = Profile
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInLine,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

