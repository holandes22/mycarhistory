from django.db import models
from django.db.models import permalink


@permalink
def get_permalink(name):
    return ('{name}'.format(**locals()), [])

class Action(object):

    def __init__(self, url, title):
        self.url = url
        self.title = title



class BaseModel(models.Model):

    class Meta:
        abstract = True

    def get_model_attrs(self, filter_fields=['id', 'pk']):
        for field in self._meta.fields:
            if field.name not in filter_fields:
                if field.choices:
                    yield field.name, getattr(self, 'get_%s_display' % field.name)
                else:
                    yield field.name, getattr(self, field.name)
