from django.contrib import admin
from .models import TestData1, TestData2, TestData3, TestData4, TestData5


# Register your models here.
class TestData1Admin(admin.ModelAdmin):
    list_display = ("name", "cost", "revenue", "profit", "roi")


admin.site.register(TestData1, TestData1Admin)


class TestData2Admin(admin.ModelAdmin):
    list_display = ("name", "cost", "revenue", "profit", "roi")


admin.site.register(TestData2, TestData2Admin)


class TestData3Admin(admin.ModelAdmin):
    list_display = ("name", "cost", "revenue", "profit", "roi")


admin.site.register(TestData3, TestData3Admin)


class TestData4Admin(admin.ModelAdmin):
    list_display = ("name", "cost", "revenue", "profit", "roi")


admin.site.register(TestData4, TestData4Admin)


class TestData5Admin(admin.ModelAdmin):
    list_display = ("name", "cost", "revenue", "profit", "roi")


admin.site.register(TestData5, TestData5Admin)
