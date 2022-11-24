from django.db import models

# Create your models here.
class Uploadphoto(models.Model):
    name=models.CharField(max_length=225)
    img=models.ImageField(upload_to='imags')
    dec=models.TextField()
    def __str__(self):
        return self.name

class Details(models.Model):
    name=models.CharField(max_length=225)
    photo=models.ImageField(upload_to='imgs')
    details=models.TextField()


class Upload_ph(models.Model):
    name = models.CharField(max_length=225)
    immg = models.ImageField(upload_to='immags')
    dec = models.TextField()

    def __str__(self):
        return self.name