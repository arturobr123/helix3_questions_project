from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    completed = models.BooleanField(default=False) #when question is answered correctly

    def _str_(self):
        return self.title