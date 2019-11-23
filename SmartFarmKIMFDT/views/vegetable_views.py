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

def update_vegetable(request):
    id = int(request.POST.get("id"))
    parsed_val = parse_keys(Plant_keys, request.POST)
    Vegetable.objects.filter(pk=id).update(**parsed_val)
    return redirect("/vegetables/view/")
    
def edit_vegetable(request, id):
    _v = Vegetable.objects.get(pk=id)
    return render(request, "edit_vegetable.html", {
        "v": _v,
    }) 
    
def del_vegetable(request):
    ids = json.loads(request.POST.get("delete-ids"))
    Vegetable.objects.filter(pk__in=ids).delete()
    return redirect("/vegetables/view/")
    
def new_vegetable(request):
    return render(request, "new_vegetable.html")

def add_vegetable(request):
    if request.method == "POST":
        parsed_val = parse_keys(Plant_keys, request.POST)
        _v = Vegetable(**parsed_val)
        _v.save()
    return redirect("/vegetables/view/")
    
def view_vegetable(request):
    _v = Vegetable.objects.all()
    return render(request, "view_vegetable.html", {"vegs": _v})