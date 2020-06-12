from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('contact/', views.contact, name='contact'),
	path('courses/', views.courses, name='courses'),
	path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
	path('courses/english', views.english, name='english'),
	path('courses/math', views.math, name='math'),
	path('courses/science', views.science, name='science'),
]
