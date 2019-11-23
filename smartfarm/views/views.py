#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
from threading import Timer
import paho.mqtt.client  as mqtt
import os
from urllib.parse import urlparse


tempPayload1 = [[0,0,0]]
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    print(msg.payload)
    stringPayload = (msg.payload.decode("utf-8"))
    print(stringPayload)
    tempPayload = stringPayload.split(',')
    tempPayload1.append(tempPayload)


def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

def print_time():
    print ("From print_time", time.time())

def print_some_times():
    print(time.time())
    Timer(20, print_time, ()).start()
    # Timer(, print_time, ()).start()
    # print(time.time())

tz = pytz.timezone('Asia/Bangkok')
list_nodes = ['X', 'A', 'B', 'C']

def unixtime_to_readable(unixtime):
    tz = pytz.timezone('Asia/Bangkok')
    now1 = datetime.fromtimestamp(unixtime, tz)
    month_name = now1.month
    thai_year = now1.year + 543
    time_str = now1.strftime('%H:%M:%S')
    return ("%d/%s/%d %s"%(now1.day, month_name, thai_year, time_str))

key = {
  "type": "service_account",
  "project_id": "smartfarming-4581d",
  "private_key_id": "56ad16c75e66fa82eee158502148b49661f96ebe",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQChEhzkeMdtMxwQ\nxbuph1JoYPPdBQgQ0x6Wuoi/ZIDGUMjJ9Z2FkZG/JYW+IIWyWADNnz/L9vTriOE+\nJCdvwpi36YrzEp5HV10Uz4xfUB/NpzbDQF1OBkn52ZVXGuAD4PjuVR1ZQmEwTb6x\nhf8sQqLMYX2rfVcis3/CzfHJAOUpuJBubZMS0/C04POEGuw4Wauycv2TZKGIB2vo\nC8mcqeABQ8e/PFEElepSZEqfbZo63/6gCi5UEX3z2JQcX1Y/G1fHkwsMJ99k5um0\n3kxe2D8X8BmFAKYPjiBxAC5b/Nh4TVxsaCZc1t21GRJ/u0cRFTJZQFtstYOUbpk9\nfgKplNyhAgMBAAECggEATPw3SwxfZVY0Z9/anmDLhpAwfsdU35XI3QozKieDVUZv\ncfgvXhQBsXbhwcoRnPhrCdy/xWE4FwvJfMYTA1vjWqQJgby4YijjmHrLARNu4AC4\nMAKnlg9zdDQHKSbzQ2dYE7Ii4PLVOR0vs/Hz0NfYsA843ap+51scCaQdmJEQ9ys4\nw4KZOaKTMaU/aDT+etIWOHcLzXbUQFZtI2YX3fn4ps2xZO6OaBGizEPuh52UPZve\ntvGXJntQeC5xJ81tbqg8axOjDJqj8IKwHILVvk+0xfYReFPe8gr4j+Uu3SYTyzln\nj8SVyinz1Bdicf39Ga52Ekj1ZbBzDhO0b8D6rwyTMQKBgQDh/sq6d27Bps/jjg6l\nwkzWnUweaDiHZQWdDcuw8HJML3+IViBNt7N85lQHiS2g6Bju22WThB6JPLzVSCNP\nDGB2KLrfJlO4a+T3PmkzOh0zE38GxkIi0PV6LOjr/9Up1KauI8zQqqoOWQm5sHRS\n9OkvuZ77/z+bxRlug9Q3R2c3gwKBgQC2dKSa+7xtn3iE+0ZxSY25C8Jg8jQpo46o\n4kQO1RC4MpwRwMk2iafrqFr4S2dmYsMrNIpWStAVaPQ+iGdmAAvD8WufEJL+1ei8\n0vKclT1kTQ6UxMfu+iBkZ1mIfrOGWpPtI1abPTXQ+jkz7GajXfLvO2BSMu3oFV22\nFvNcbnF+CwKBgExvtvW2a3mICAw5Ae9CdmaoMRSfv27b1jg2cExaJu5pqkLcjnR6\ny3RVGtqppQslNTmkbwijyQg1yNCCY57a2s1cHUhYWDyqEXkmXMJ8x199GpuZ9sh7\n0GsQQX+AugI58F45sY5qCrZrmwR5D/724t/HcmRdApCW63EbmW1Q8zItAoGAffwa\n8R1kJfnYmVJ8eJtGbgENri1wEVRrnHfocKl0ywu/Mo8BIVR6C8ILVqmSc2M8yqeT\n4jP0bOQ0yr0bUJY1iY45NvOV3LtN4pxyg+aVJp4CtH0QZRZ3qXynmRWL1vjSbgtZ\nsQXaFDvDpfPVh3bG2aQRRZD/L6MZOzOrxSZJ3bMCgYA708mqDy4DXVayjD7RUAUy\noRMSuNlUB9d8ps+ZE9JOaNEp3/KadynquCbE1P6CxM33CKjR5X1oZ9tI5ElnDzFh\nMj1obPEY1u6ayZLzs9HQWd9xj/7iY41O/4up+k1A1vvuyGNbUKO9aFvp9hmV4JZr\nalBIUP9XHs5lDGg1eWauXA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-93q0p@smartfarming-4581d.iam.gserviceaccount.com",
  "client_id": "110147095966425260255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-93q0p%40smartfarming-4581d.iam.gserviceaccount.com"
}


cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://smartfarming-4581d.firebaseio.com/'
})

def index(request):
    refA = db.reference('A')
    resultA = refA.order_by_child('time').limit_to_last(1).get()
    for key, val in resultA.items():
        a_air_humidity = val["data"]["air_humidity"]
        a_air_temperature = val["data"]["air_temperature"]
        a_light_intensity = val["data"]["light_intensity"]
        a_pm25 = val["data"]["pm25"]

    _v = Vegetable.objects.all()
    _p = Plant.objects.all()
    p_data = []
    for i in _p:
        di = {}
        di["start_plant_timestamp"] = i.start_plant_timestamp.strftime("%d/%m/%Y")
        year = int(i.start_plant_timestamp.strftime("%Y"))-543
        day = i.start_plant_timestamp.strftime("%d")
        month = i.start_plant_timestamp.strftime("%m")
        time = str(day)+"/"+str(month)+"/"+str(year)
        date_time_obj = datetime.strptime(time, '%d/%m/%Y')
        dif_time = (datetime.now() - date_time_obj)
        if(int(dif_time.days) <=  0):
            d = 0
        else:
            d = dif_time.days
        di["plant_type"] = i.plant_type
        di["sensor"] = i.sensor
        di["id"] = i.id
        di["duration"] = d
        p_data.append(di)

    refStatus = db.reference('Valve_Status')
    valve1 = str(refStatus.child('Valve1').get())
    valve2 = str(refStatus.child('Valve2').get())
    if valve1 == "off":
        state1 = "false"
        _b1 = ""
    else:
        state1 = "true"
        _b1 = "active"
    if valve2 == "off":
        state2 = "false"
        _b2 = ""
    else:
        state2 = "true"
        _b2 = "active"
    return render(request, "index.html", {
        "vegs": _v,
        "plant": p_data,
        "state1": state1,
        "button1": _b1,
        "state2": state2,
        "button2": _b2,

        "a_air_humidity": a_air_humidity,
        "a_air_temperature": a_air_temperature,
        "a_light_intensity": a_light_intensity,
        "a_pm25": a_pm25,
    })
def control(request):
    data_dict = {}
    refA = db.reference('A')
    resultA = refA.order_by_child('time').limit_to_last(1).get()
    for key, val in resultA.items():
        data_dict["a_air_humidity"] = val["data"]["air_humidity"]
        data_dict["a_air_temperature"] = val["data"]["air_temperature"]
        data_dict["a_soil_temperature"] = val["data"]["light_intensity"]
        data_dict["a_soil_moisure"] = val["data"]["pm25"]
        data_dict["a_time"] = unixtime_to_readable(val["time"])
    return render(request, "control.html", data_dict)


def history(request):
    _p = Plant.objects.filter(is_harvested=True)
    _v = Vegetable.objects.all()
    data = []
    for i in _p:
        data.append(i.plant_type)
    data = set(data)

    return render(request,"history.html", {"plant":_p, "vegs":_v, "dataset":data})

def view_history(request):
    p_t = request.POST.get("p_t")
    if(p_t == "all"):
        _p = Plant.objects.all()
    else:
        _p = Plant.objects.filter(is_harvested=True, plant_type=p_t)
    p_data = []
    node_val = []
    for i in _p:
        di = {}
        di["start_date"] = i.start_plant_timestamp.strftime("%d/%m/%Y")
        di["end_date"] = i.end_plant_timestamp.strftime("%d/%m/%Y")
        di["plant_type"] = i.plant_type
        di["sensor"] = i.sensor
        di["id"] = i.id
        di["totals"] = str(i.keep_total)+" "+i.keep_unit
        if( i.sensor == u'ตู้ต้นแปลง' ):
            node = "C"
        elif(i.sensor == u'ตู้กลางแปลง'):
            node = "B"
        else:
            node = "A"
        value = get_value_from_date(di["start_date"], di["end_date"], node, di["id"])
        node_val.append(value)
        p_data.append(di)
    _c = Compost.objects.all()
    c_data = []
    i=1
    for v in _c:
        di = {}
        di["id"] = v.pk
        di["p_id"] = v.plant_id
        di["number"] = i
        di["date"] = v.compost_date.strftime("%d/%m/%Y")
        di["type"] = v.compost_type
        di["totals"] = str(v.compost_total) + " " + v.compost_unit
        di["total"] = v.compost_total
        di["unit"] = v.compost_unit
        c_data.append(di)
        i= i+1

    return render(request,"view_history.html", {"p_t":p_t ,"plant":p_data, "compost":json.dumps(c_data), "history":json.dumps(p_data), "node_val":json.dumps(node_val)})

def del_history(request):
    v_id = request.POST.get("p_t")
    ids = json.loads(request.POST.get("delete-ids"))
    Plant.objects.filter(pk__in=ids).delete()
    return redirect("/history/")

def valve(request):
    refA = db.reference('Valve_Status')
    valve1 = str(refA.child('Valve1').get())
    valve2 = str(refA.child('Valve2').get())
    if valve1 == "off":
        state1 = "false"
        _b1 = ""
    else:
        state1 = "true"
        _b1 = "active"
    if valve2 == "off":
        state2 = "false"
        _b2 = ""
    else:
        state2 = "true"
        _b2 = "active"
    return render(request, "valve.html", {
        "state1": state1,
        "button1": _b1,
        "state2": state2,
        "button2": _b2,
    })

def valve_state(request):
    valve = db.reference('Valve_Status')

    v = int(request.GET.get('valve'))
    s = str(request.GET.get('status'))
    if v == 1:
        if s == "on":
            print("on1")

            valve.update({
                'Valve1': 'on'
            })
        elif s == "off":
            print("off1")
            valve.update({
                'Valve1': 'off'
            })

    elif v == 2:
        if s == "on":
            print("on2")
            valve.update({
                'Valve2': 'on'
            })
        elif s == "off":
            print("off2")
            valve.update({
                'Valve2': 'off'
            })
    return HttpResponse("")

def graph(request):
    refA = db.reference('A')
    result_a = refA.order_by_child('time').limit_to_last(1500).get()
    a_array_json_air_humid = []
    a_array_json_air_temp = []
    a_array_json_soil_moisure = []
    a_array_json_soil_temp = []
    for key, val in result_a.items():
        a_json_air_humid = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_humidity"]
                            }
        a_json_air_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["air_temperature"]
                            }
        a_json_soil_moisure = {'x' : val["time"]*1000,
                            'y' : val["data"]["pm25"]
                            }
        a_json_soil_temp = {'x' : val["time"]*1000,
                            'y' : val["data"]["light_intensity"]
                            }
        a_array_json_air_humid.append(a_json_air_humid)
        a_array_json_air_temp.append(a_json_air_temp)
        a_array_json_soil_moisure.append(a_json_soil_moisure)
        a_array_json_soil_temp.append(a_json_soil_temp)



    return render(request, "graph.html", {
                                          "a_air_humidity": json.dumps(a_array_json_air_humid),
                                          "a_air_temperature": json.dumps(a_array_json_air_temp),
                                          "a_soil_moisure": json.dumps(a_array_json_soil_moisure),
                                          "a_soil_temperature": json.dumps(a_array_json_soil_temp),
                                          })

def get_value_from_date(start, end, node, p_id):

    date_start = []
    date_end = []
    date_start = start.split("/")
    date_start[2] = int(date_start[2])-543
    time = date_start[0]+"/"+date_start[1]+"/"+str(date_start[2])
    date_start_obj = datetime.strptime(time, '%d/%m/%Y')
    unix_date_start = date_start_obj.strftime("%s")

    date_end = end.split("/")
    date_end[2] = int(date_end[2])-543
    time = date_end[0]+"/"+date_end[1]+"/"+str(date_end[2])
    date_end_obj = datetime.strptime(time, '%d/%m/%Y')
    unix_date_end = date_end_obj.strftime("%s")


    ref = db.reference(node)
    result = ref.order_by_child('time').start_at(int(unix_date_start)).end_at(int(unix_date_end)).get()
    time = []
    air_humidity = []
    air_temperature = []
    soil_temperature = []
    soil_moisure = []
    for key, val in result.items():

        air_humidity.append(val["data"]["air_humidity"])
        air_temperature.append(val["data"]["air_temperature"])
        soil_temperature.append(val["data"]["soil_temperature"])
        soil_moisure.append(val["data"]["soil_moisure"])

    value = {"p_id" : p_id,
             "air_humid_avg" : round(np.mean(air_humidity),2),
             "air_humid_max" : round(np.amax(air_humidity),2),
             "air_humid_min" : round(np.amin(air_humidity),2),

             "air_temp_avg" : round(np.mean(air_temperature),2),
             "air_temp_max" : round(np.amax(air_temperature),2),
             "air_temp_min" : round(np.amin(air_temperature),2),

             "soil_moi_avg" : round(np.mean(soil_moisure),2),
             "soil_moi_max" : round(np.amax(soil_moisure),2),
             "soil_moi_min" : round(np.amin(soil_moisure),2),

             "soil_temp_avg" : round(np.mean(soil_temperature),2),
             "soil_temp_max" : round(np.amax(soil_temperature),2),
             "soil_temp_min" : round(np.amin(soil_temperature),2)
             }
    return value
