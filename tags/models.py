from django.db import models
from django.contrib.contenttypes.models import ContentType  # allows generic relationship (based on content type)
from django.contrib.contenttypes.fields import GenericForeignKey  # allows generic relationship, defines a content object, a foriengkey

# Create your models here.
class Tag(models.Model):
    """defines a tag with label char field"""
    label = models.CharField(max_length=255)

class TagItem(models.Model):
    """The tag model """
    # what tag is applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # content obj field
    content_object = GenericForeignKey()
