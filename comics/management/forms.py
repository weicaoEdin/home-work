#coding=utf-8
from django.forms import ModelForm
from models import *
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class registration_form(forms.Form):
		
	username = forms.CharField(max_length=256,label="用户名")
	password = forms.CharField(max_length=256,label="密码",widget=forms.PasswordInput)
	email = forms.CharField(max_length=256,label="邮箱")
	
	def clean_username(self):
		name = self.cleaned_data['username']
		try:
			User.objects.get(username=name)
			raise forms.ValidationError('用户名已被使用')
		except ObjectDoesNotExist:
			pass	
		return name
		
class member_form(ModelForm):
	
	class Meta:
		model = Member
		
	exclude = ['user']
