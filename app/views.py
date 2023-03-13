from django.shortcuts import render
from django.views import View
import random

from .models import TestData1, TestData2, TestData3, TestData4, TestData5


class AppView(View):
    def get(self,
            request):
        template = 'app/app.html'
        data = TestData1.objects.all().values()

        context = {}
        context['heading'] = "Das ist ein test"
        context['pageview'] = "das hier ist auch ein test"
        context['data'] = data

        nr = 1
        for add in range(20):
            name = 'campaign' + str(nr)
            cost = round(random.uniform(200, 400), 2)
            revenue = round(random.uniform(100, 700), 2)
            profit = round(revenue - cost, 2)
            roi = round((revenue - cost) / cost * 100, 2)
            nr += 1
            break
            enter = TestData1(name=name, cost=cost, revenue=revenue, profit=profit, roi=roi)
            enter.save()

        return render(request, template, context)
