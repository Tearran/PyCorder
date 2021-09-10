#!/usr/bin/python3
# -*- coding: utf-8 -*-

from _SciClass import *
import sqlite3
import os
import psutil
import multiprocessing
from datetime import datetime

# get current local time
now = datetime.now()

#  read as epoch time
id_timestamp = datetime.timestamp(now)

# get system temprature
try:
  with open("/sys/class/thermal/thermal_zone0/temp", "r") as temp:
    tempCels = int(temp.read()[:2])
except:
  print('failed to get cpu temp')
#from _SciClass import Weather
cpu_temp = Weather(tempCels)

print(id_timestamp,",",cpu_temp.temp,"C,",now)

#database = CreatDB()
#database.CREAT_TABLE()

#p1 = Person("Joey", 50)
#print(p1.name,p1.age)
#print(cpu_temp.temp)

#app.get_webpage()