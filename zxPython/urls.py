#coding:utf8
"""zxPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from django.views.generic import TemplateView


import xadmin
from users.views import LoginView,RegisterView,ActiveUserView,ForgetView,ResetView,ModifyPwdView
from organization.views import OrgListView
from django.views.static import serve
from zxPython.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$',RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='active_code'),
    url(r'^forget/$',ForgetView.as_view(), name="forget_pw"),
    url(r'^reset/(?P<reset_code>.*)/$',ResetView.as_view(),name='reset_code'),
    url(r'^modifypwd/$',ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构url配置
    url(r'^org/', include('organization.urls',namespace='org')),

    #配置上传文件图片的访问处理函数
    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),

]
