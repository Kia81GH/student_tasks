from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_page'),
    path('all-assignments/', views.assignment_list, name='assignment_list'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('assignments/<int:assignment_id>/', views.assignment_detail, name='assignment_detail'),
]