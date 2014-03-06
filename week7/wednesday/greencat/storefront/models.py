from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    inventory = models.PositiveIntegerField()
    hero_picture = models.ImageField(upload_to="product_hero_images")
    picture_thumbnail = models.ImageField(upload_to="product_thumbnails")
    price = models.DecimalField(decimal_places=2, max_digits=6)
    video = models.FileField(upload_to="product_videos", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    sku = models.CharField(max_length=100)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name