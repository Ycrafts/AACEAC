from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        "username",
        "email",
        "is_staff",
    )
    
    fieldsets = (
        (None,{"classes": ("wide",),"fields": ("username","email","password"),},),
    )
    
    add_fieldsets = (
        (None,{"classes": ("wide",),"fields": ("username","email","password1", "password2"),},),
    )
    
admin.site.register(CustomUser, CustomUserAdmin)