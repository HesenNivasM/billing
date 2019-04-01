from django.shortcuts import render

# Create your views here.
def dashboardPanel(request):
    return render(request, 'dashboard/dashboardPanel.html')