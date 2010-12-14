from django.db import models
from cms.models import CMSPlugin
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers 

STYLE_CHOICES = map(lambda x: (x,x), get_all_styles())

LANGUAGE_CHOICES = map(lambda x: (x[1][0], x[0]), get_all_lexers())
LANGUAGE_CHOICES.sort(lambda x,y: cmp(x[0], y[0]))

class PygmentsPlugin(CMSPlugin):
    code_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    style = models.CharField(max_length=255, choices=STYLE_CHOICES)
    linenumbers = models.BooleanField()
