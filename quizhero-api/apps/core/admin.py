from django.contrib import admin

from apps.core.models import UUIDUser as User

admin.site.register(User)
