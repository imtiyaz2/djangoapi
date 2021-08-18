from django.urls import path
from .views import *
urlpatterns=[
    path('createmployee',create_employee),
    path('getallrecapi',get_allrecord),
    path('filterrecapi',filter_record),
    path('delrecapi',delete_record),
    path('updaterec',update_record)
]