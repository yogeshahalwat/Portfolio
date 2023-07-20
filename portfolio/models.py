from django.db import models

class user(models.Model):
    name=models.CharField(max_length=100)
    memo=models.TextField()
    image=models.ImageField(upload_to='uploads',blank=True)
    date=models.DateField()

    def __str__(self):
        return self.name

