from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Weapon(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Armor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdventureGear(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mounts(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Potions(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Trinkets(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Need to set these up as choices
# class Dice(models.model):
#     # 
#     type = models.CharField(max_length=4)

#     def __str__(self):
#         return self.name

# class Coins(models.model):
#     # 
#     type = models.CharField(max_length=4)

#     def __str__(self):
#         return self.name