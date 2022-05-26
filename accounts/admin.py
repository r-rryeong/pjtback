from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_login', 'is_superuser',)


admin.site.register(get_user_model(), UserAdmin)