from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=1)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(allow_unicode=True, unique=True)
    id = models.AutoField(primary_key=True)

    def save(self, *args, **kwargs):
        if self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
