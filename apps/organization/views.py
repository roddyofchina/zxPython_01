#coding:utf8
from django.shortcuts import render,HttpResponse
from django.views.generic import View

from .models import CityDict,CourseOrg
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import UserAskForm


# Create your views here.

class OrgListView(View):
    def get(self,request):

        all_orgs = CourseOrg.objects.all()

        hot_orgs = all_orgs.order_by("-click_nums")[:3]

        city_id = request.GET.get('city','')

        category = request.GET.get('ct',"")

        sort = request.GET.get('sort','')

        if sort:
            if sort == "students":
                all_orgs=all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs=all_orgs.order_by("-course_nums")

        if category:
            all_orgs = all_orgs.filter(category=category)


        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)

        all_citys = CityDict.objects.all()

        org_nums = all_orgs.count()

        return render(request,'org-list.html',{'all_orgs':orgs,
                                               'all_citys':all_citys,
                                               'org_nums':org_nums,
                                               'city_id': city_id,
                                               'category':category,
                                               'hot_orgs':hot_orgs,
                                               'sort':sort,
                                               })



class AddUserAskView(View):
    '''
        用户添加咨询
    '''
    def post(self,request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)
            return HttpResponse('{"status":"success"',content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":u"添加错误"}',content_type='application/json')



