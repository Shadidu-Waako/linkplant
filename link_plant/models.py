from django.db import models

# Create your models here.

# Profile table -> Name, slug, bg_color
class Profile(models.Model):
    BG_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
        ('black', 'Black'),
        ('white', 'White'),
        ('cyan', 'Cyan'),
        ('magenta', 'Magenta'),
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name

# Link table -> Text, url, profile
class Link(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')