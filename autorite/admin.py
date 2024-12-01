from django.contrib import admin

from autorite.models import Autorite

# Register your models here.
# admin.site.register(Autorite)

@admin.register(Autorite)
class AutoriteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'addresse')