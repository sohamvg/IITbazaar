from django.contrib import admin
from accounts.models import Profile
# Register your models here.

from .models import Profile

admin.site.register(Profile)