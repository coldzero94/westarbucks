from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=50)

	class meta:
		db_table = 'categories'

class SubCategory(models.Model):
	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True)

	class meta:
		db_table = 'sub_categories'

class Drink(models.Model):
	name_en = models.CharField(max_length=100)
	name_kr = models.CharField(max_length=100)
	description = models.TextField(max_length=3000)
	thumbnail = models.URLField(max_length=500)
	serving = models.DecimalField(max_digits=4, decimal_places=1)
	claories = models.DecimalField(max_digits=5, decimal_places=1)
	saturated_fat = models.DecimalField(max_digits=4, decimal_places=1)
	protein = models.DecimalField(max_digits=4, decimal_places=1)
	sodium = models.DecimalField(max_digits=4, decimal_places=1)
	sugar = models.DecimalField(max_digits=4, decimal_places=1)
	caffein = models.DecimalField(max_digits=4, decimal_places=1)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
	allergy = models.ManyToManyField('Allergy', through= 'DrinkAllergy')

	class meta:
		db_table = 'drinks'

class Allergy(models.Model):
	name = models.CharField(max_length=50)

class DrinkAllergy(models.Model):
	drink = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)
	allergy = models.ForeignKey('Allergy', on_delete=models.SET_NULL, null=True)

	class meta:
		db_table = 'drink_allergies'