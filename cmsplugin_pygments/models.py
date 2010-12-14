from django.db import models
from cms.models import CMSPlugin
from pygments.style import STYLE_MAP

STYLE_CHOICES = map(lambda x: (x,x), STYLE_MAP.keys())

class PygmentsPlugin(CMSPlugin):
    code_language = models.CharField(max_length=20)
    code = models.TextField()
    style = models.CharField(max_length=255, choices=STYLE_CHOICES)
