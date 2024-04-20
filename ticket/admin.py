from django.contrib import admin

# Register your models here.
from ticket.models import User, Bus, Seat, Transaction

admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(Bus)
admin.site.register(Seat)
