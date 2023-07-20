from django.shortcuts import render
from .models import user

# Create your views here.

def home(request):
    data=user.objects.all()
    context={"data":data}
    return render(request,"portfolio/home.html",context)
