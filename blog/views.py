from django.shortcuts import render,get_object_or_404
from .models import blog

def Blog(request):
    #data=blog.objects.all()
    #data=blog.objects.order_by("-date")[:3]   # 3 record will show with decreasing order
    data=blog.objects.order_by
    context={"data":data}
    return render(request,"blog/blog.html",context)

def detail(request,pk):
    data=get_object_or_404(blog,pk=pk)
    return render(request,"blog/detail.html",{"data":data})