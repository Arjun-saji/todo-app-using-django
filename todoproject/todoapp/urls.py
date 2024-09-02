from django.urls import path
from . import views

urlpatterns=[ path("",views.index,name="index"),
path("addtask/",views.addtask,name="addtask"),
path("edit/<int:task_id>/",views.edittask,name="edittask"),
path("delete/<int:task_id>/",views.deletetask,name="deletetask"),
]