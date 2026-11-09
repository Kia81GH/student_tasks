from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Course, Assignment

# Create your views here.

def home_page_view(request):
        """
        رندر کردن صفحه اصلی که فقط منوی ناوبری را نشان می دهد.
        """
        # اگر می خواهید hello world نمایش داده شود، context اضافه کنید
        # context = {'message': 'به سامانه خوش آمدید'}
        # return render(request, 'assignments/base.html', context)
        
        # اگر می خواهید کاملا خالی باشد، context ندهید
        return render(request, 'assignments/base.html') 

def assignment_list(request):
    """
    1. نمایش همه تکالیف مرتب‌شده بر اساس مهلت تحویل (deadline)
    """
    assignments = Assignment.objects.select_related('course').order_by('deadline')
    context = {
        'assignments': assignments,
        'now': timezone.now(),
    }
    return render(request, 'assignments/assignment_list.html', context)

def course_list(request):
    """
    2. دریافت و نمایش فهرست تمامی درس‌ها
    """
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'assignments/course_list.html', context)

def course_detail(request, course_id):
    """
    3. نمایش اطلاعات یک درس خاص و فقط تکالیف مربوط به همان درس
    (همراه با خطای 404 در صورت نامعتبر بودن شناسه درس)
    """
    course = get_object_or_404(Course, pk=course_id)
    assignments = Assignment.objects.filter(course=course).order_by('deadline')
    context = {
        'course': course,
        'assignments': assignments,
        'now': timezone.now(),
    }
    return render(request, 'assignments/course_detail.html', context)

def assignment_detail(request, assignment_id):
    """
    5. نمایش اطلاعات کامل یک تکلیف انتخاب‌شده
    (همراه با خطای 404 در صورت نامعتبر بودن شناسه تکلیف)
    """
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    now = timezone.now()
    is_expired = assignment.deadline < now

    context = {
        'assignment': assignment,
        'now': now,
        'is_expired': is_expired,
    }
    return render(request, 'assignments/assignment_detail.html', context)
