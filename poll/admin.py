from django.contrib import admin
from .models import Poll

admin.site.register(Poll)

def __str__(self):
    return self.field_name
