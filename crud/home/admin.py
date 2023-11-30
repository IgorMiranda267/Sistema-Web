from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser, create_groups

create_groups()

admin.site.register(CustomUser, UserAdmin)

admin.site.unregister(Group)  
admin.site.register(Group)
