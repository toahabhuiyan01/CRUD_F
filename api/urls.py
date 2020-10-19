from django.urls import path
from . import views
urlpatterns = [
    path('task-list/', views.taskList),
    path('task-sin/<str:pk>/', views.taskSingle),
    path('task-create/', views.taskCreate),
    path('task-update/<str:pk>/', views.taskUpdate),
    path('task-delete/<str:pk>/', views.taskDelete),
]
