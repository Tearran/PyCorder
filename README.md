# Sensors, Backend
### Sensor
To log and record data in stages.

## Stages 
1. Formate data TBD: ($TEMP, Flatfile)
2. Record formated data TBD: options(SQLite, CVS, other)
3. Store and migrate data to remote server TBD: options(MongoDB, MySQL, PostgreSQL) - usage public, historical, AI predictive)  


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


## T0 B3 D373RM4ND

- Creat generic flatfile DB to hold sensor data
- research `#import multiprocessing`
- research `#import os`
- research `#import psutil`
- [open weather map](https://openweathermap.org/api) integration
- a lot

# Contributors

## Special thanks to the following people and their education projects:

- ShotokuTech: [git](https://github.com/ShotokuTech)  [youtube](https://www.youtube.com/c/ShotokuTech)
- adafruit: [web](https://learn.adafruit.com/)
- DroneBot Workshop: [web](https://dronebotworkshop.com/)
- MicroPython [web](http://micropython.org/)


 
 
