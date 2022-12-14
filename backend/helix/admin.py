from django.contrib import admin

from .models import Question
from .models import Comment

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'completed')


# Register your models here.

admin.site.register(Question, QuestionAdmin)
