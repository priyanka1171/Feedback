from django.shortcuts import render
from .forms import EnForm
from .models import EnModel


def home(request):
	if request.method=="POST":
		data=EnForm(request.POST)
		if data.is_valid():
			data.save()
			fm=EnForm()
			return render(request,"home.html",{"fm":fm,"msg":"we will get to you"})
	else:
		fm=EnForm()
		return render(request,"home.html",{"fm":fm})
