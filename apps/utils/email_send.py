#!/usr/bin/env python
#coding:utf-8

__author__ = 'Luodi'

from users.models import  EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from zxPython.settings import DEFAULT_FROM_EMAIL

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = "Python自学网在线注册激活"
        email_body = "请点击下面的链接激活你的帐号:http://127.0.0.1:8000/active/{0}".format(code)

        send_status=send_mail(email_title,email_body,DEFAULT_FROM_EMAIL,[email,],fail_silently=True)
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = "Python自学网在线密码重置连接"
        email_body = "请点击下面的链接重置密码:http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email, ], fail_silently=True)
        if send_status:
            pass




