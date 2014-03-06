from django.contrib.auth.models import User
from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User)
    posted = models.DateTimeField(auto_now=True)
    url = models.SlugField()
    category = models.ForeignKey(BlogCategory)
    tags = models.ManyToManyField(BlogTag)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    post = models.ForeignKey(BlogPost)