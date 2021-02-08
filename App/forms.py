from django import forms
from App.models import Bus, Student, Booking, Contact
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User #default django user creation model

#definging busform
class BusForm(forms.ModelForm):
	class Meta:
		model = Bus
		fields = "__all__"

#defining studentform
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = "__all__"

#defining booking form
class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = ['seat_number','travel_time','source','destination','student_id']

#defining usercreation form
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']

#contact form		
class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'subject', 'message']

#defining signup forms
class SignUp(forms.Form):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Username'})) #username
	password = forms.CharField(widget = forms.PasswordInput()) #password input