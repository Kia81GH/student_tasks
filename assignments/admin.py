from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali
from .models import Course, Assignment

#register
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'teacher')
    search_fields = ('title', 'code', 'teacher')


class AssignmentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # ستون‌هایی که در جدول نمایش داده می‌شوند
    list_display = ('title', 'course', 'get_deadline_jalali', 'get_created_at_jalali')
    search_fields = ('title', 'description', 'course__title')
    list_filter = ('course', 'deadline')

    # نمایش تاریخ مهلت به صورت شمسی در لیست
    @admin.display(description='مهلت تحویل (شمسی)')
    def get_deadline_jalali(self, obj):
        if obj.deadline:
            return datetime2jalali(obj.deadline).strftime('%Y/%m/%d - %H:%M')
        return '-'

    # نمایش تاریخ ثبت به صورت شمسی در لیست
    @admin.display(description='تاریخ ثبت (شمسی)')
    def get_created_at_jalali(self, obj):
        if obj.created_at:
            return datetime2jalali(obj.created_at).strftime('%Y/%m/%d - %H:%M')
        return '-'


admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)

