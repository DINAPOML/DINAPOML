from django.db import models

class Registration(models.Model):
	Name = models.CharField(max_length=300)
	ContactNumber = models.CharField(max_length=300)
	Age = models.CharField(max_length=300)
	Address = models.CharField(max_length=300)
	EmailAddress = models.CharField(max_length=300)
	class meta:
	 	db_table="AdoptorInfo"
			
class DogList(models.Model):
	Gender = models.CharField(max_length=300)
	Breed = models.CharField(max_length=300)
	Fur = models.CharField(max_length=300)
	Category = models.CharField(max_length=300)
	class meta:
		db_table="DogList"

class DogAdoption(models.Model):
	aId = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)
	DateToday = models.DateField(default=None, blank=False)
	DateToAdopt = models.DateField(default=None, blank=False)
	Remarks = models.DateField(default=None, blank=False)
	class meta:
		db_table="DogAdoption"

class DogDonation(models.Model):
	aId = models.ForeignKey(Registration, default=None, on_delete=models.CASCADE)
	Amount = models.DateField(max_length=300)
	DateTransaction = models.DateField(default=None, blank=False)
	Message = models.DateField(default=None, blank=False)
	Status = models.DateField(default=None, blank=False)
	class meta:
		db_table="DogDonation"







		