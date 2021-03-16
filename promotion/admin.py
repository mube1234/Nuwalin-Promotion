from django.contrib import admin
from .models import *
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Add_News)
admin.site.register(Profile)
admin.site.register(SalesPromotion)
admin.site.register(PromotionCategory)
admin.site.register(Adertising)
admin.site.register(AttachPromotion)
admin.site.register(Fqa)
admin.site.register(MoneyQuestion)
admin.site.register(PromotionView)

