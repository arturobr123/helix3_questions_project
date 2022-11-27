from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    completed = models.BooleanField(default=False) #when question is answered correctly

    def _str_(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE , related_name='comments')
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    created_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.text
    
    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True