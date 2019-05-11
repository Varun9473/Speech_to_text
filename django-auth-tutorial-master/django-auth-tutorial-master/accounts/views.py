from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *
from django.core.exceptions import ValidationError
from django.contrib import messages

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Fileupload(request):
	d = fileupload.objects.all()
	
	form = fileform()

	# with open('data.txt', 'r') as file:
    # 	data = file.read().replace('\n', '')

	data={'form':form , 'data':d }
	if(request.method=="POST"):
		try:
			f=fileform(request.POST,request.FILES)
			f.save()
			messages.success(request, 'File uploaded successfully!')
		except Exception as e:
			raise ValidationError('File is not supported')
			#return render(request,'home.html',{'e':e })
	return render(request,'home.html',data)


