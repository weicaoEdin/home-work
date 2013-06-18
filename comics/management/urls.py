from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('management.views',
                       url(r'^$', 'redirect_to_list', name="root"),
                       url(r'^login/$','login', {"template_name":"login.html"},name="login", ),
                       url(r'^logout/$','logout_then_login', {"login_url":"/comics/login/"}, name="logout", ),
                       url(r'registration/$','registration', name="registration"),
                       url(r'member_profile/$','member_profile',name="member_profile"),
                       url(r'list/$','list', name="upload_list"),
                       url(r'management/$','management',name="management"),
                       
			)