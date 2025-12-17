from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from accounts.models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ("email", "last_name", "first_name", "nickname", "is_active", "created_at")
    list_display_links = ()
    list_filter = ("is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("last_name", "first_name", "nickname",)}),
        ("Permissions", {"fields": ("is_active", "is_superuser",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "last_name", "first_name", "nickname", "password1", "password2")
        })
    )
    search_fields = ("email", "last_name", "first_name", "nickname")
    ordering = ("-created_at",)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)