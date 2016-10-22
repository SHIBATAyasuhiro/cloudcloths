from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from fav.models import Favorite
from taggit.managers import TaggableManager


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    product_img1 = models.ImageField(upload_to='images/')
    product_img2 = models.ImageField(upload_to='images/', null=True)
    product_img3 = models.ImageField(upload_to='images/', null=True)
    product_img4 = models.ImageField(upload_to='images/', null=True)
    product_img5 = models.ImageField(upload_to='images/', null=True)
    product_caption = models.CharField(max_length=200)
    product_detail_text = models.TextField()
    product_brand = models.CharField(max_length=200, default="no-brand")
    favorites = GenericRelation(Favorite)
    tags = TaggableManager()

    def __unicode__(self):
        return self.product_name


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

