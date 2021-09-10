#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from datetime import datetime

now = datetime.now() # current date and time

time = now.strftime("%I:%M:%S")
print("time:", time)

date = now.strftime("%m/%d/%Y")
print("date:",date)
