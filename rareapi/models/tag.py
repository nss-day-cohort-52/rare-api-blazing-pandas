class Tag():
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, label):
        self.id = id
        self.label = label
        
from django.db import models



class Tag(models.Model):
    label = models.CharField(max_length=55)
    