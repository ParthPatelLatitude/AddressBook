from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(utl_status)

class UserSignupAdmin(admin.ModelAdmin):
    list_display = ('email_id',)

admin.site.register(UserSignup, UserSignupAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

admin.site.register(UserProfile, UserProfileAdmin)



class SqlLoginAdmin(admin.ModelAdmin):
    list_display = ('action','created_date_time')

admin.site.register(SqlLogin,SqlLoginAdmin)