from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType  # allows generic relationship (based on content type)
from django.contrib.contenttypes.fields import GenericForeignKey  # allows generic relationship, defines a content object, a foriengkey

# Create your models here.
class  LikedItem(models.Model):
    """model what user liked what item"""
    # if a user is deleted, all objects that the user has liked too is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericForeignKey()
