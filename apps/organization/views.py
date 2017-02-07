#coding:utf8
from django.shortcuts import render
from django.views.generic import View

from .models import CityDict,CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class OrgListView(View):
    def get(self,request):

        all_orgs = CourseOrg.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)

        all_citys = CityDict.objects.all()

        org_nums = all_orgs.count()

        return render(request,'org-list.html',{'all_orgs':orgs,'all_citys':all_citys,'org_nums':org_nums})


