#!/usr/bin/env python
#coding:utf-8
import xadmin

__author__ = 'Luodi'

from .models import  Course,Lesson,Video,CourseResource

class CourseAdmin(object):

    list_display = ['name', 'students', 'fav_nums', 'click_nums','degree','desc','learn_times']
    search_fields = ['name', 'degree', 'image',]
    list_filter = ['name', 'students', 'image', 'degree','add_time']

class LessonAdmin(object):

    list_display = ['course', 'name', 'add_time',]
    search_fields = ['name', 'course', ]
    list_filter = ['course__name', 'name', 'add_time',]

class VideoAdmin(object):

    list_display = ['lesson', 'name', 'add_time', ]
    search_fields = ['name', 'course', ]
    list_filter = ['lesson', 'name', 'add_time', ]

class CourseResourceAdmin(object):

    list_display = ['course', 'name', 'add_time', 'download']
    search_fields = ['name', 'course', ]
    list_filter = ['course', 'name', 'add_time', 'download']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)


