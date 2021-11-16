from django.contrib import admin
from .models import Movie,Actor, Review
# from acounts.models import User


# Register your models here.

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Review)
# admin.site.register(User)