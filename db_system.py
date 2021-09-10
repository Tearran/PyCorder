#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import sqlite3
import time
import random
import sqlite3

sqlite3.connect('weather.db')
#ID	OW_TEMP	OW_HUMIDITY	OW_PRESSURE	OW_COVER																					

def CREAT_TABLE():
    conn = sqlite3.connect('weather.db')
    print ("Opened database successfully")
    conn.execute('''CREATE TABLE OPEN_WEATHER
             (ID   INT PRIMARY KEY     NOT NULL,
             TIMESTAMP   INT  NOT NULL,
             TEMPERATURE   INT  NOT NULL,
             HUMIDITY      INT  NOT NULL,
             ATMOSPHERIC   INT  NOT NULL,
             CLOUD_COVER   TEXT);''')
    print ("Table created successfully")
    conn.close()
try:
  CREAT_TABLE()
except:
  pass

print("5")
Print('4')