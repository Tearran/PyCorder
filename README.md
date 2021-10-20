# PyCorder
### Python Sensor Recorder 

PyCorder is intended to be a back end to log and record data in stages.

## Stages 

1. Format to dicionanry (XML, JSON, CSV) - usage (SBC display, LED indicators, smart apps)
2. Record formated data to Flatfile DB (SQLite, CVS, other) - usage (Time > 1 s/ms, passed averages, charts/plots)  
3. Store DB size/time trigger to migrate Flatfile data to git-repo or DB server (MongoDB, MySQL, PostgreSQL) - usage public, historical, AI predictive)  


## Requierments:

```sh 
#!/usr/bin/python3 
# -*- coding: utf-8 -*- 
import os
import multiprocessing
import time
import psutil
import spidev as SPI
from lib import ST7789
```


## Confirmed working:
- Getting system Epoch time to use as BD unique id
- Getting CPU temperature to use as real data 
- Creating and implementing a class
- Creating a CSV entry
- creating a database and tables


## todo
- add micro controler
- Remove as many Libs as possible
- Creat generic flatfile DB to hold sensor data
- research `#import multiprocessing`
- research `#import os`
- research `#import psutil`
- [open weather map](https://openweathermap.org/api) integration
- [MicroPython](http://micropython.org/) support
- a lot

# Contributors

Special thanks to the following people and their education projects:

- ShotokuTech: [git](https://github.com/ShotokuTech)  [youtube](https://www.youtube.com/c/ShotokuTech)
- adafruit: [web](https://learn.adafruit.com/)
- DroneBot Workshop: [web](https://dronebotworkshop.com/)
- MicroPython [web](http://micropython.org/)


 
[SocialArtCasts](http://socialartcasts.com)  
