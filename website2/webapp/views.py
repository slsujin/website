from django.shortcuts import render

from .models import table2


# Create your views here.
def web1(request):
    obj=table2.objects.all()
    return render(request,"index.html",{'result':obj})

