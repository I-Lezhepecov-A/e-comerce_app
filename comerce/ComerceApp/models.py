from django.db import models

class Search(moldels.Model):
    search=models.CharField(max_length=200)