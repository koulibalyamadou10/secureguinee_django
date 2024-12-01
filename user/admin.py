from django.contrib import admin

from user.models import SCUser

# Register your models here.
# admin.site.register(SCUser)

@admin.register(SCUser)
class SCUserAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'numero')