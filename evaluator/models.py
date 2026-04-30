from django.db import models

class Evaluation(models.Model):
    prompt = models.TextField()
    response1 = models.TextField()
    response2 = models.TextField()

    accuracy = models.IntegerField()
    relevance = models.IntegerField()
    coherence = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)