# PyCorder
### Python Sensor Recorder 

PyCorder is intended to be a back end to log and record data in stages. 

## Stages 

1. record to flat-file (txt, JSON) - usage local usage (SBC display, LED indicators, smart apps)
2. record to  DB (SQLite, CVS) - usage (averages, charts)  

3. DB size/time trigger to migrate DB data to git-repo or DB server (MongoDB, MySQL, PostgreSQL) - usage public, historical,  


## Requierments:

```sh 
#!/usr/bin/python3 
# -*- coding: utf-8 -*- 

#include sqlite3
```


## Confirmed working:

- Creating and implementing a class
- creating a database and tables with sqlite3 
- logging temperature (CPU) 

## todo
- Creat generic DB to hold sensor data
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
