from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task, TaskDetail
from datetime import date
from django.db.models import Q

# Create your views here.
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")

def test(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)

def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm() # For Get method

    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """ For Model Form Data"""
            form.save()

            return render(request, 'task_form.html', {"form": form, "message": "Task added successfully"})

            '''For Django Form Data'''
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assign_to = data.get('assign_to')

            # task = Task.objects.create(
            #     title= title, description = description, due_date = due_date)
            # #Assign employee to task
            # for emp_id in assign_to:
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assign_to.add(employee)

            # return HttpResponse("Task Added Successfully")

        
    context = {"form": form}
    return render (request, 'task_form.html', context)

def view_task(request):
    # tasks = Task.objects.filter(status= 'PENDING')

    # tasks = Task.objects.filter(due_date = date.today())

    # tasks = TaskDetail.objects.exclude(priority= 'L')
    """Show the task contains paper and status pending"""
    # tasks = Task.objects.filter(title__icontains="c", status="PENDING") 

    # tasks = Task.objects.filter(Q(status = 'PENDING') | Q(status = 'IN_PROGRESS'))

    # tasks = Task.objects.filter(status="sdfsdf").exists() 

    # tasks = Task.objects.all()
    tasks = Task.objects.select_related('details').all()

    return render(request, 'show_task.html', {"tasks": tasks})