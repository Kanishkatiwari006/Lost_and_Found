from django.contrib import admin

# Register your models here.
from .models import found
from .models import lost
from .models import contacts

admin.site.register(found)
admin.site.register(lost)
admin.site.register(contacts)
