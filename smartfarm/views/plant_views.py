#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Plant, Vegetable, Compost
from ..post_data import parse_keys, Plant_keys,parse_keys2, parse_keys3, parse_keys4
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
from datetime import datetime, timedelta
import time
import requests
import pytz
import numpy as np

tz = pytz.timezone('Asia/Bangkok')
database_types = ['X', 'A', 'B', 'C']

def keep_plant(request):
    if request.method == "POST":
        id = int(request.POST.get("p_id"))
        time = str(request.POST.get("keep-date")) 
        date = datetime.strptime(time, '%d/%m/%Y')
        total = request.POST.get("keep-total")
        unit = request.POST.get("keep-unit")
        parsed_val = parse_keys4(date, total, unit)
        Plant.objects.filter(pk=id).update(**parsed_val)
    return redirect("/")
    
def del_plant(request):
    id = int(request.POST.get("delete-id"))
    Plant.objects.filter(pk=id).delete()
    return redirect("/")
    
def add_plant(request):
    if request.method == "POST":
        time = str(request.POST.get("start-plant-timestamp")) 
        date_time_obj = datetime.strptime(time, '%d/%m/%Y')
        parsed_val = parse_keys2(request.POST.get("plant-type"), date_time_obj, request.POST.get("sensor"))
        _p = Plant(**parsed_val)
        _p.save()
    return redirect("/")
    
def view_compost(request, id):
    _c = Compost.objects.filter(plant_id=id)
    _p = Plant.objects.get(pk=id)
    c_data = []
    i=1
    for v in _c:
        di = {}
        di["id"] = v.pk
        di["number"] = i
        di["date"] = v.compost_date.strftime("%d/%m/%Y")
        di["type"] = v.compost_type
        di["totals"] = str(v.compost_total) + " " + v.compost_unit
        di["total"] = v.compost_total
        di["unit"] = v.compost_unit
        c_data.append(di)
        i= i+1
    
    return render(request, "view_compost.html", {"compost": c_data , "plant":_p ,"c_js": json.dumps(c_data)})
    
def add_compost(request):
    if request.method == "POST":
        time = str(request.POST.get("compost-date")) 
        c_date = datetime.strptime(time, '%d/%m/%Y')
        p_id = request.POST.get("p_id")
        c_type = request.POST.get("compost-type")
        c_total = request.POST.get("compost-total")
        c_unit = request.POST.get("compost-unit")
        parsed_val = parse_keys3(p_id, c_date, c_type, c_total, c_unit)
        _c = Compost(**parsed_val)
        _c.save()
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)
    
def del_compost(request):
    p_id = int(request.POST.get("p_id"))
    ids = json.loads(request.POST.get("delete-ids"))
    Compost.objects.filter(pk__in=ids).delete()
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)
    
def edit_compost(request):
    id = int(request.POST.get("c_id"))
    p_id = request.POST.get("p_id")
    time = str(request.POST.get("compost-date")) 
    c_date = datetime.strptime(time, '%d/%m/%Y')
    c_type = request.POST.get("compost-type")
    c_total = request.POST.get("compost-total")
    c_unit = request.POST.get("compost-unit")
    parsed_val = parse_keys3(p_id, c_date, c_type, c_total, c_unit)
    Compost.objects.filter(pk=id).update(**parsed_val)
    html = "/plant/view_compost/"+str(p_id)+"/"
    return redirect(html)