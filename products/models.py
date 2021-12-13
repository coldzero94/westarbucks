from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

class Categories(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)

class Drinks(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    kr_name = models.CharField(max_length=45)
    en_name = models.CharField(max_length=45)
    description = models.TextField()

class Allergy(models.Model):
    name = models.CharField(max_length=45)

class Allergy_drink(models.Model):
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)

class Images(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey(Drinks, on_delete=models.CASCADE)

class Sizes(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

class Nutritions(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink = models.ForeignKey(Drinks, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Sizes, on_delete=models.SET_NULL, null=True)