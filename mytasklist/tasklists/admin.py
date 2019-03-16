from django.contrib import admin

# Local
from .models import Tasks

# Registrando os Models
admin.site.register(Tasks)