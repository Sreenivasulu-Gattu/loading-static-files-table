from django.shortcuts import render

# Create your views

def table(request):
    return render(request,'table_pro.html')