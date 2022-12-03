from django.contrib import admin
from . models import anime
from . models import more_anime

# Register your models here.

admin.site.register(anime)
admin.site.register(more_anime)


