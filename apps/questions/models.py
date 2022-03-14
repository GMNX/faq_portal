from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer  = models.TextField()
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.answer
