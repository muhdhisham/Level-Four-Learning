from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    
    '''
    This cuts out all values of "arg" from string
    '''

    return value.replace(arg,"")



    
# register.filter('cut',cut)
# 1st argument is what we wish to call the templatetag in  html
# 2nd argument is actual name of the function

