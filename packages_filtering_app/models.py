from django.db import models

class Package(models.Model):
    author = models.EmailField()
    email = models.EmailField(default='')
    description = models.TextField()
    title = models.CharField(max_length=200)
    keywords = models.TextField(default='')
    version = models.TextField(default='')
    maintainer = models.TextField(default='')
    link = models.URLField()
    guid = models.URLField()
    pub_date = models.DateTimeField()
