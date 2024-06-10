from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    list_editable = ('is_active',)
