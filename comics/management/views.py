# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext
from models import *
from forms import *
from django.utils import timezone
import os
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth.decorators import login_required

@login_required
def redirect_to_list(request):
        return redirect('login')


def registration(request):
	if request.method == "POST":
		form = registration_form(request.POST)
		if form.is_valid():
			user_data = form.cleaned_data
			user = User.objects.create_user(
				 user_data["username"],
				 user_data["email"],
				 user_data["password"]
				 )
			return redirect("member_profile")
	else:
		form = registration_form()	
	
	return render_to_response('registration_form.html',{"form":form},RequestContext(request),)
	
	
	
def member_profile(request):
	if request.method == "POST":
		form = member_form(request.POST)
		if form.is_valid():
		
			profile = form.save(commit=false)
			profile.user = request.user
			profile.save()
			return redirect("list")
	else:
		form = member_form()
			
	return render_to_response('member_profile.html',{'form':form},RequestContext(request),)	
	
	
def management(request):
	return render_to_response('management.html',RequestContext(request),)


def list(request):

	data = Member.objects.all()
	return render_to_response('list.html',{'data':data},RequestContext(request),)
