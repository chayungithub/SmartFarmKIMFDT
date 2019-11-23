"""smartfarm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import views, user_views, vegetable_views, plant_views

urlpatterns = [
    # common views
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^control/', views.control),
    url(r'^graph/', views.graph),
    url(r'^history/', views.history),
    url(r'^delete_history/', views.del_history),
    url(r'^view_history/', views.view_history),
    url(r'^meter/', views.control),
    url(r'^valve/', views.valve),
    url(r'^valve_state/', views.valve_state),

    # vegetable views
    url(r'^vegetables/view/', vegetable_views.view_vegetable),
    url(r'^vegetables/new/', vegetable_views.new_vegetable),
    url(r'^vegetables/add/', vegetable_views.add_vegetable),
    url(r'^vegetables/delete/', vegetable_views.del_vegetable),
    url(r'^vegetables/update/', vegetable_views.update_vegetable),
    url(r'^vegetables/edit/(?P<id>[0-9]+)', vegetable_views.edit_vegetable),

    # plant views
    url(r'^plant/add/', plant_views.add_plant),
    url(r'^plant/keep/', plant_views.keep_plant),
    url(r'^plant/compost/', plant_views.add_compost),
    url(r'^plant/edit_compost', plant_views.edit_compost),
    url(r'^plant/view_compost/(?P<id>[0-9]+)', plant_views.view_compost),
    url(r'^plant/delete/', plant_views.del_plant),
    url(r'^plant/delete_compost/', plant_views.del_compost),

    # user views
    url(r'^signin/', user_views.signin),
    url(r'^login/', user_views.login),
    url(r'^makelogin/', user_views.make_login),
    url(r'^logout/', user_views.logout),
    url(r'^user/change_password/', user_views.change_password),
    url(r'^user/change_email/', user_views.change_email),
]
