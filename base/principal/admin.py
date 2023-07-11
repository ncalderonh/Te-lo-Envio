from django.contrib import admin
from django.contrib.auth.models import User
from .models import Usuario, Productor

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']

admin.site.unregister(User)  # Desregistrando la configuración predeterminada
admin.site.register(User, CustomUserAdmin)  # Registrando la configuración personalizada


admin.site.register(Usuario)
admin.site.register(Productor)