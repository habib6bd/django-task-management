from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")