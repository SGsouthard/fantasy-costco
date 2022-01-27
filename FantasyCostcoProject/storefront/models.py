from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

DICE_CHOICES = [
    ('D4', 'd4'),
    ('D6', 'd6'),
    ('D8', 'd8'),
    ('D10', 'd10'),
    ('D12', 'd12'),
    ('D20', 'd20'),
    ('D100', 'd100'),
]

# Create your models here.
class Weapon(models.Model):
    itemname = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # format (2 d6 + 3)
    amountofdice = models.IntegerField()
    dicetype = models.CharField(max_length=4, choices=DICE_CHOICES)
    modifier = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class WeaponForm(ModelForm):
    class Meta:
        model = Weapon
        fields = ['itemname', 'description', 'price', 'amountofdice', 'dicetype', 'modifier', 'user']

class Armor(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    stats = models.CharField(max_length=500)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdventureGear(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mount(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Potion(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Trinket(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

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