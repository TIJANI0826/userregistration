from django import forms
from django.forms import fields, models
from .models import Package,Laundry,Members,TicketNumber
from django.db import transaction

class CreateNewList(forms.ModelForm):
    class Meta:
        model = Package
        fields = ( "name_event", "is_approved")

class OrderLaundryForm(forms.ModelForm):
    class Meta:
        model = Laundry
        exclude = ('user',"dropp_off",)

    # @transaction.atomic
    # def save(self):
    # order = Laundry.objects.create(user=user)
    #     return order
