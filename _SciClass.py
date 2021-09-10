#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Weather:
  def __init__(self, temp):
    self.temp = temp


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Application:
    def __init__(self):
        pass
    def get_webpage(self):
        print('From application')

class CreatDB:
  def __init__(self):
    pass
    
  def CREAT_TABLE(self):  
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