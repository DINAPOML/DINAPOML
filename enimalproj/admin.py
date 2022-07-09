from django.contrib import admin
from .models import *

admin.site.register(Registration)
admin.site.register(DogList)
admin.site.register(DogAdoption)
admin.site.register(DogDonation)