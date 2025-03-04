from django.urls import path
from tasks.views import ManagerDashboardView, EmployeeDashboardView, create_task, ViewTaskListView, update_task, task_details, dashboard, Greetings, HiGreetings, HiHowGreetings, CreateTask, ViewProject, TaskDetail, UpdateTask, DeleteTaskView

urlpatterns = [
    # path('manager-dashboard/', manager_dashboard, name="manager-dashboard"),
    path("manager-dashboard/", ManagerDashboardView.as_view(), name="manager-dashboard"),
    # path('user-dashboard/', employee_dashboard, name='user-dashboard'),
    path("employee-dashboard/", EmployeeDashboardView.as_view(), name="employee-dashboard"),
    # path('create-task/', create_task, name='create-task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    # path('view_task/', view_task, name='view-task'),
    path('view-task/', ViewTaskListView.as_view(), name='view-task'),
    # path('task/<int:task_id>/details/', task_details, name='task-details'),
    path('task/<int:task_id>/details/',
         TaskDetail.as_view(), name='task-details'),
    # path('update-task/<int:id>/', update_task, name='update-task'),
    path('update-task/<int:id>/', UpdateTask.as_view(), name='update-task'),
    # path('delete-task/<int:id>/', delete_task, name='delete-task'),
    path('delete-task/<int:id>/', DeleteTaskView.as_view(), name='delete-task'),
    path('dashboard/', dashboard, name='dashboard'),
    path('greetings/', HiHowGreetings.as_view(greetings='Hi Good Day!'), name='greetings')
]