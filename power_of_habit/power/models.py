from django.db import models

# Create your models here.
class Habit(models.Model):
	day = models.IntegerField(default = 1)
	habit1 = models.CharField(max_length = 25)
	habit2 = models.CharField(max_length = 25)
	habit3 = models.CharField(max_length = 25)
	habit4 = models.CharField(max_length = 25)
	habit5 = models.CharField(max_length = 25)
	habit6 = models.CharField(max_length = 25)
	habit7 = models.CharField(max_length = 25)
	habit8 = models.CharField(max_length = 25)



