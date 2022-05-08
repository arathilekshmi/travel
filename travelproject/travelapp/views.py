from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def demo(request):
    # return HttpResponse("Hellowww World")
    #    name="Python"
       obj=Place.objects.all()
       team = Team.objects.all()
       return render(request,"index.html",{'object':obj,'team':team})
# def demos(request):
#         team=Team.objects.all()
#         return render(request,"index.html",{'team':team})
# def alloper(request):
#         return render(request,"result.html")
