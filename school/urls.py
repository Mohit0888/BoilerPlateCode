from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from school import views

urlpatterns = [
    #path('getstudent', views.get_student),
    #path('poststudent', views.post_student),
    #path('student/<int:pk>', views.detail_student),
    path('', views.StudentView.as_view()),
    path('/<int:pk>', views.StudentView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)