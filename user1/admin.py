from django.contrib import admin
from .models import Laundry, Members,TicketNumber,Package
# Register your models here.
admin.site.register(Laundry)
admin.site.register(TicketNumber)
admin.site.register(Members)
admin.site.register(Package)