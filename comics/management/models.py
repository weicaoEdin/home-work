#coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

	member_type_choices = (
		("JG","监管"),
		("ZZ","制作"),
		("MT","媒体"),
		("GG","广告"),
		("WL","网络"),
	)
	member_level_choices = (
		("SUPER_USER","超级管理员"),
		("ADMIN","系统管理员"),
		("STUFF","业务管理员"),
		("AREA_ADMIN","大区监管"),
		("LOCAL_ADMIN","地区监管"),
		("TRADER","观察会员"),
		
	)
	bank_name_choices = (
	
		("NB","宁波银行"),
		("ZG","中国银行"),
		("GS","工商银行"),
		("NY","农业银行"),
		("JS","建设银行"),
		("ZS","招商银行"),
		
	)
	
	area_part_choices = (
		
		("NORTH","北方"),
		("WEST","西部"),
		("EAST","华东"),
		("SOUTH","华南"),
		("OTHER","其他"),
	
	)

	user = models.OneToOneField(User)
	
	company = models.CharField(max_length=512)
	
	
	area_part = models.CharField(max_length=256,choices = area_part_choices,verbose_name="所在区域")
	#area_province = models.CharField(max_length=256,choices = area_province_choices)
	area_city = models.CharField(max_length=256,verbose_name="城市")
	
	start_date = models.DateField(verbose_name="开始日期")
	
	valid_date = models.DateField(verbose_name="有效期")
	
	member_type = models.CharField(max_length=256,choices = member_type_choices,verbose_name="会员类型")
	member_level = models.CharField(max_length=256, choices = member_level_choices,verbose_name="会员等级")
	IP = models.IPAddressField(verbose_name="IP地址")
	serial_number = models.CharField(max_length=256,verbose_name="序列号");
	
	authorisor_name = models.CharField(max_length=256,verbose_name="授权人姓名")
	authorisor_id = models.CharField(max_length=256,verbose_name="授权人身份证号")
	authorisor_phone = models.CharField(max_length=256,verbose_name="授权人手机号")
	
	authorisor_check_name = models.CharField(max_length=256,verbose_name="授权复核人姓名")
	authorisor_check_id = models.CharField(max_length=256,verbose_name="授权复核人身份证号")
	authorisor_check_phone = models.CharField(max_length=256,verbose_name="授权复核人电话")
	
	obeservor_number = models.CharField(max_length=256,verbose_name="观察会员人数")
	
	bank_name = models.CharField(max_length=256,choices = bank_name_choices,verbose_name="保证金开户行")
	bank_acount = models.CharField(max_length=256,verbose_name="银行账号")
	
	
	
	
	
	


# Create your models here.
