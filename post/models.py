from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=25, blank=False)
    content = models.TextField()
    unique_id = models.TextField(null=True)
