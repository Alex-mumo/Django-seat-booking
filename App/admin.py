from django.contrib import admin
#importing the model to admin site
from App.models import Student , Bus, Booking , Contact

# Register your models here.
admin.site.register(Student)
admin.site.register(Bus)
admin.site.register(Booking)
admin.site.register(Contact)
