import os
from django import template
 
register = template.Library()
 
@register.filter
def getfilename(value):
    print("******************")
    print(value)
    return os.path.basename(value.file.name)