from django.contrib import admin
from jdztuser.models import BossExpUser
# Register your models here.
class BossExpUserAmin(admin.ModelAdmin):
	list_display = ['Uin','NickName','UserType','JdCompanyName','GdtUId']
	search_fields = ['Uin','NickName','GdtUId']
	list_filter = ['UserType','DelFlag','FundType','MasterFlag']

admin.site.register(BossExpUser,BossExpUserAmin)