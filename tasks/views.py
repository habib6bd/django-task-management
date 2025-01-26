from django.http import HttpResponse
from django.shortcuts import render
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
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
    #retrieve all data from task model
    tasks = Task.objects.all() 

    #retrive a specific task
    task_3 = Task.objects.get(id=1)
    return render(request, 'show_task.html', {"tasks": tasks, "task_3": task_3})