from django import template
from promotion.views import get_all_users,get_entertainment,get_fqa

register=template.Library()
@register.inclusion_tag('promotion/get_all_users.html')
def all_users():
    return {'all_users':get_all_users()
            }
@register.inclusion_tag('promotion/get_count_entertainment.html')
def all_entertainment():
    return {'all_entertainment':get_entertainment()
            }
@register.inclusion_tag('promotion/get_fqa.html')
def all_fqa():
    return {'all_fqa':get_fqa()
            }
