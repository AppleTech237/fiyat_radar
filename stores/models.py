from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=100)
    website_url = models.URLField()
    logo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name