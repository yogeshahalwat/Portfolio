from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateField(blank=True)

    def __str__(self):
        return self.title