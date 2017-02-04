#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'


import xadmin
from xadmin import views

from .models import UserProfile,EmailVerifyRecord,Banner



class BaseSetting(object):
    #打开主题功能
    enable_themes = True
    use_bootswatch  =True


class GlobalSettings(object):
    site_title = "Python自学网后台系统"
    site_footer = "Python自学网"
    #menu_style = "accordion"



class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email']
    list_filter = ['send_type','send_time']


class BannerAdmin(object):

    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url',]
    list_filter = ['title', 'image', 'url', 'index','add_time']


xadmin.site.register(UserProfile)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)





