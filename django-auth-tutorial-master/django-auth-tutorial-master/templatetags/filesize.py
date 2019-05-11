from django import template

register = template.Library()

@register.filter(name='filesize')
def filesize(value):
    if value is None:
        return ''
    if value <= 1024 and value >= 999:
    	return str(value/1024) + ' KB'
    if value >= 1024**2:
    	return str(round(value/1024**2, 3))+' MB'
    else:
    	return str(value)+' bytes'


