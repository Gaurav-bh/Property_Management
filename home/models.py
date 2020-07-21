from django.db import models

# Create your models here.
class service(models.Model):
    image=models.ImageField(upload_to="home/")
    title=models.CharField(max_length=30)
    des=models.TextField()

    def __str__(self):
        return self.title