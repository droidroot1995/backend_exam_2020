from django.urls import path, re_path
from django.urls import include
from users.views import (create_user, create_student, 
                        create_teacher, students_list, 
                        teachers_list, search_by_id, search_by_name)

urlpatterns = [
    path('add_usr', create_user, name='add_user'),
    path('add_stud', create_student, name='add_stud'),
    path('add_teach', create_teacher, name='add_teach'),
    path('stud_lst', students_list, name='stud_lst'),
    path('teach_lst', teachers_list, name='teach_lst'),
    path('sbid', search_by_id, name='sbid'),
    path('sbname', search_by_name, name='sbname'),
]