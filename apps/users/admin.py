# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    models = User
    list_display = [
        "pkid",
        "email",
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["id", "email"]
    list_filter = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    fieldsets = (
        (
            _("login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Persmissions and Groups"),
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Important Dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )

    search_fields = ["email", "username", "first_name", "last_name"]


admin.site.register(User, UserAdmin)
