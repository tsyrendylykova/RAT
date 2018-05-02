from django.db import models
from django.utils import timezone

class Test(models.Model):
    word1 = models.CharField(max_length=50)
    word2 = models.CharField(max_length=50)
    word3 = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.word1, self.word2, self.word3, self.answer