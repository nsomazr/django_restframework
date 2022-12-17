from django.db import models

# Create your models here.

class HumanQuery(models.Model):

    human_query = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.human_query


class AIResponse(models.Model):

    ai_response = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ai_response