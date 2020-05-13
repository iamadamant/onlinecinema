from django.contrib import admin
from films.models import *

# Register your models here.

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Comment)