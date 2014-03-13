from django.contrib.auth.models import User
from django.db import models


class Media(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="media_files", null=True, blank=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "{0} owned by {1}".format(self.name, self.user)