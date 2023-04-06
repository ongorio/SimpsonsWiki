from django.db import models
from django.utils.text import slugify
from pathlib import Path

def charcter_image_handler(instance, filename):
    result = 'characters'
    extension = Path(filename).suffix
    
    result = Path(result, instance.name + extension)
    result = str(result)

    return result

# Create your models here.
class Character(models.Model):
    name = models.CharField('Name', max_length=255, unique=True)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    full_name = models.CharField('Full Name', max_length=500)
    nationality = models.CharField('Nationality', max_length=255)
    description = models.TextField('Description')
    occupation = models.CharField('Occupation', max_length=255)
    first_appearance = models.CharField('First Appearance', max_length=255)
    release_year = models.IntegerField('Release Year')
    image = models.ImageField('Image', upload_to=charcter_image_handler)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)