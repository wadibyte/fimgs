import uuid
import os
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import (GenericForeignKey,
                                                GenericRelation)


class Fimg(models.Model):

    def user_directory_path(instance, filename):
        name, ext = os.path.splitext(filename)
        uuid_ = uuid.uuid4()
        uuid_ = str(uuid_).replace('-', '')
        if instance.create_by is None:
            return 'images_0/{0}{1}'.format(uuid_, ext)
        return 'image_{0}/{1}{2}'.format(instance.create_by.id, uuid_, ext)

    content_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.SET_NULL,)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    create_by = models.ForeignKey(
                        settings.AUTH_USER_MODEL, null=True, blank=True,
                        related_name="%(app_label)s_%(class)s_create_by",
                        on_delete=models.SET_NULL,)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.ImageField(verbose_name='Image',
                              upload_to=user_directory_path)
    is_active = models.BooleanField(default=False)

    # tags = TaggableManager(blank=True)

    def as_dict(self):
        return {
            'image': self.image.url,
            'width': self.image.width,
            'height': self.image.height,
            'size': self.image.size,
            'ext': os.path.splitext(self.image.name)[-1],
            }
