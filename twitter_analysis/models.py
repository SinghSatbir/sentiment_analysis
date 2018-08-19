from django.db import models

# Create your models here.
class Word(models.Model):
    keyword_entered=models.CharField(max_length=128)

    def __str__(self):
        return self.keyword_entered