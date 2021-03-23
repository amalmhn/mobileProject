from django.db import models

class MobileModel(models.Model):
    phone_name = models.CharField(max_length=120)
    memory = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(default='Pending',max_length=120)
    date = models.DateField(editable=False,auto_now=True)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.phone_name