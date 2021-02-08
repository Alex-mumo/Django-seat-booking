from django.db import models

# Create your models here.

#student model
class Student(models.Model):
	student_id = models.CharField(max_length = 255, primary_key = True)
	phone_no = models.IntegerField(blank = False)
	student_name = models.CharField(max_length = 255)
	class Meta:
		db_table = "student" #student database

#bus model
class Bus(models.Model):
	number_plate = models.CharField(max_length = 255, primary_key = True)
	seat_number = models.IntegerField()
	class Meta:
		db_table = "bus" #database name 
     
#booking model
class Booking(models.Model):
	#booking_id = models.CharField(max_length = 255)
	seat_number = models.IntegerField(primary_key = True)
	travel_time = models.DateTimeField()
	source = models.CharField(max_length = 255)  
	destination = models.CharField(max_length = 255)
	student_id  = models.CharField(max_length = 255,  blank = False)
	class Meta:
		db_table = "booking" #database nam

class Contact(models.Model):
	name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	subject = models.CharField(max_length = 255)
	message = models.CharField(max_length = 255)
	class Meta:
		db_table = "contact"
