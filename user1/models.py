from django.db import models
import os
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.urls import reverse
from django.conf import settings
from django.db.models.signals import post_save
from . choice import *
from . utils import code_generator
import uuid
# import barcode 
from django.core.files import File 
# import qrcode 
# from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.core.validators import RegexValidator

# Create your models here.
class Package(models.Model):
    
	name_event	=models.CharField(
		max_length=200
	)

	is_approved = models.BooleanField(default=False)
	
	def get_absolute_url(self):
		return reverse('event_details', kwargs={'pk': self.pk})
	def __str__(self):
		return self.name_event
	class Meta():
		verbose_name ="Packages"
		
	
	
#""" MODEL FOR BOOKING TICKET """


    
    
class Members(models.Model):
    name		= models.CharField(
		max_length=200
	)
    phone_number		=models.IntegerField(
		
	)
    gender = models.CharField(
				max_length=30
	)
    date_of_birth	=models.DateTimeField(
		
		verbose_name='Date Of Birth'
	)	
    plan				=models.ForeignKey(
		Package, on_delete=models.CASCADE, 
	)
    reason_for_registering = models.CharField(
        null=True,max_length=100
    )
    start_date	=models.DateTimeField(
		
		verbose_name='Registration Date'
	)
    exp_date	=models.DateTimeField(
		
		verbose_name='Expiring Date'
	)
    barcode	=models.ImageField(
		
		upload_to='barcodes', blank = True
	)
    refered_by  = models.CharField(max_length=200)		
    
    def __str__(self):
        return self.name
	# def save(self, *args, **kwargs):
	# 	qrcode_img = qrcode.make(self.name)
	# 	canvas = Image.new('RGB', (290, 290), 'white')
	# 	draw = ImageDraw.Draw(canvas)
	# 	canvas.paste(qrcode_img)
	# 	frame = f'qr_code-{self.name}'+'.pgn'
	# 	buffer = BytesIO
	# 	canvas.save(buffer, 'PNG')
	# 	self.qrcode.save(fname, File(buffer), save=False)
	# 	canvas.close()
	# 	super().save(*args, **kwargs)
		
	
   # """MODELS FOR GENERATING TICKET NUMBER """
class TicketNumber(models.Model):
	ticket 	=models.ForeignKey(Members, on_delete=models.CASCADE, editable=False)
	ticket_number	=models.CharField(max_length=120, editable=False)
	expired  = models.BooleanField(default=False)
	class Meta():
		verbose_name = 'Ticket Number '
	def get_absolute_url(self):
 		return reverse('ticketdetail', kwargs={'pk': self.pk})
	def save(self, *args, **kwargs):
		self.ticket_number = code_generator()
		super(TicketNumber, self).save(*args, **kwargs)
	def __str__(self):
		return self.ticket.name



#    """MODELS FOR LAUNDRY"""

class Laundry(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True) # <--- added

	customer_name       =models.CharField(max_length=50, verbose_name='Customer Name')
	custom_number       = models.IntegerField(verbose_name='Customer Number')
	shirt               = models.IntegerField(verbose_name='T-Shirt', null = True, blank=True,)
	trouser             = models.IntegerField(verbose_name='Trouser/Short', null = True, blank=True,)
	underwear           = models.IntegerField(verbose_name='Single/Boxers', null = True, blank=True,)
	native              = models.IntegerField(verbose_name='Complete Native', null = True, blank=True,)
	duvet               = models.IntegerField(verbose_name='Duvet', null = True, blank=True,)
	duver_beddings      = models.IntegerField(verbose_name='Duvet and Beddings', null = True, blank=True,)
	towel               = models.IntegerField(verbose_name='Towel', null = True, blank=True,)
	dropp_off           = models.DateTimeField(auto_now=True, null = True, blank=True,)
	commission          = models.CharField(max_length=200, verbose_name='Refered Byss', null = True, blank=True,)
	
	def __str__(self):
		return self.customer_name
	
	def orderAmount(self):
		shirt = self.shirt
		trouser = self.trouser
		underwear = self.underwear
		native = self.native
		duvet = self.duvet
		duver_beddings = self.duvet_beddings
		towel = self.towel
		dropp_off = self.dropp_off
		commission = self.commission

		return (shirt,trouser,underwear,native,duvet,duver_beddings,towel,dropp_off,commission)