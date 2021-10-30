# Raspberry pi Zero OS Modification
The following documentation is based on a bash script ( located below )

## Intro:

>The script is an attempt to increase performance and or stability while learning sharing results on the way. 

 Customizing OS experiment:
Completed:
- update && upgrade system
- Install Python3 node.js pip3 etc
- make and test hello world node.js 
- rip SD card to img
- burn img to 16+gig sd exspant and test.

TODO:
1. Change boot logo
2. Test kernel - (later modules experiments)
3. Copy new kernel to 4 gig SD card (replicate above steps) 
	a. rip SD card to img
  b. burn img to 16+gig sd exspant and test.



## Setup
### Requierments
- The basic setup to ssh into your pi.
- build tools
- build Time
	- an extra pi or 2 to cut it
- text editing
	- nano : is used in the following examples
  - vim
  - bash echo >
  - etc
- ssh
	- putty
  - ?????
- Time

### Tools & source

> Start with a fresh Raspberry Pi OS lite image.
> or not…  \\_O_/

The build tools
```bash 
sudo apt install git bc bison flex libssl-dev make
```
download git source code .....

```bash
git clone --depth=1 https://github.com/raspberrypi/linux
```


> the flag --depth=1 (as i understand it) will allow us to only download the latest code and not the history of the code in its entirety 




### Configure
Configure the build

Change into the downloaded directory
```bash 
cd linux 
``` 
set for 32bit kernel: [Ref](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#configuring-the-kernel)

```
KERNEL=kernel 
```
set for 1 core: [Ref](https://www.raspberrypi.com/documentation/computers/linux_kernel.html#configuring-the-kernel)

```
make bcmrpi_defconfig

```
#### menuconfig
> make menuconfig is one of five similar tools that can configure Linux source
> - https://en.wikipedia.org/wiki/Menuconfig

##### requirements
ncurses (toto link)

```bash
sudo apt install libncurses5-dev
```

> While waiting for this  
check out some ref links at the bottom
```
make menuconfig
```


## Custom Logo
Creat a logo
### Tools
- https://fixthephoto.com/online-gimp-editor.html
- TODO


```bash

#!/bin/bash
clear

while true; do
 cat << "EOF"
https://sunnyspot.org/asciiart/gallery/startrek.html


                 ______
              _-' .   .`-_
          |/ /  .. . '   .\ \|
         |/ /            ..\ \|
       \|/ |: .   ._|_ .. . | \|/
        \/ |   _|_ .| . .:  | \/
       \ / |.   |  .  .    .| \ /
        \||| .  . .  _|_   .|||/
       \__| \  . :.  .|.  ./ |__/
         __| \_  .    .. _/ |__
          __|  `-______-'  |__
             -,____  ____,-
               ---'  `---
    This will step you through the ...

Do you wish to continue(Y/n)?

EOF

    read -p  '>> '  yn
    case $yn in
        [Yy]* ) clear; break;;
        [Nn]* ) exit;;
        * )  clear ;  break;;
    esac
done
sudo apt update
while true; do
 cat << "EOF"

    LKARS Kernel Configuration
             TR-560
 ________.--------------.________
|  ||__| [_]|                    |
|  |     [_]|                    |
|__|_____[_]|____________________|
| |PWR |  | F1 |-DATA  | I || E ||
| |STBY|  |_F2_| SENSE-|___||___||
|_|[__]|_________________________|
|           ___________________  |
| [ALPHA]  |                   | |
| [BETA ]  |                   | |
| [GAMMA]  |                   | |
| [DELTA]  |                   | |
|  _____   |                   | |
| |^ H B|  |___________________| |
| || H ||  .-DEVICE INPUT--.  _  |
| || H ||  |               | [_] |
| || H ||   GEO   MET   BIO  [_] |
| |A_H_v|  [___] [___] [___] [_] |
|________________________________|
|__[][][][]____________[][][][]__|
|  ____________________________  |
| |.-COM XMISSION---.   ______ | |
| | ________________  E|\ __ /|| |
| ||ACCEPT|INTERSHIP| M| |  | || |


Installing git bc bison flex libssl-dev make 

continue(Y/n)?

EOF

    read -p  '>> ' yn
    case $yn in
        [Yy]* ) clear;  break;;
        [Nn]* ) exit;;
        * )  clear ;   break;;
    esac
done

sudo apt install git bc bison flex libssl-dev make

while true; do
clear
 cat << "EOF"

                  .',.                  
                 'dKKO:.                
                ,OX:::~o.               
               ;O::::::::.              
              ;0:::::::::d.             
             ,~~~:0::~~dO~d.            
            '~:O;.o~NO:.l~;l.           
           .o;;c;:dOOO;;;::0;           
           :0:;;......;O:::::'          
    .';:``o0:::;Odll`l:0:::::;l`-:,.    
  .-o-;'.'d::::;;:;O;;:O;::::O;..,-ol.  
 .dd.    ';::::;;l----o0::::N;-    .do. 
 .od'. ..o;::::;-,,,,,;d0:::::;;...::-. 
  .:lo:O0;::::::;,,,,,,:;::::::;0;o:'   
     .-;:::::::0o:,,,;:d0:::::::;;.     
       ';N::::::;0;dooodO;:::::0;       
       ,O::::::;Oo:'..  .l;;0:::l       
       l::::::;;.        .oO-:oOd.      
      .:::;O;0;           '::' ..       
      ';Oo;lOl.            ;O:.         
      .,. ,;:.              -0d.        
      .,',:0:               .o;:;,,.    
     .::;;:d.                ,O:::;-    
      '-d:o'                  ;ool;.   


Downlod Kernel source from
https://github.com/raspberrypi/linux

then, Go Grab a Pepsi

continue(Y/n)?

EOF

    read -p  '>> ' yn
    case $yn in
        [Yy]* ) clear; break;;
        [Nn]* ) exit;;
        * )  clear ;   break;;
    esac
done

git clone --depth=1 https://github.com/raspberrypi/linux
echo 'Change directory '
cd linux

while true; do
 cat << "EOF"

https://ascii.co.uk/art/science
  
__________________________________________________________________________

    .-.                                                               .-.
   /   \           .-.                                 .-.           /   \
  /     \         /   \       .-.     _     .-.       /   \         /     \
-/-------\-------/-----\-----/---\---/-\---/---\-----/-----\-------/-------\--
          \     /       \   /     `-'   `-'     \   /       \     /
           \   /         `-'                     `-'         \   /
            `-'                                               `-'
     _________________________________________________________________
GUI Kernel configuration

continue(Y/n)?

EOF

    read -p '>> ' yn
    case $yn in
        [Yy]* ) clear ; break;;
        [Nn]* ) exit;;
        * )  clear ;  break;;
    esac
done


echo 'Set Arch to 32Bit'
KERNEL=kernel

echo 'Set CPU Core 1'
make bcmrpi_defconfig

while true; do
 cat << "EOF"
by bord Tearran 
                                                 
                       ...                      
                    ...:S%:;.                   
               ..  ..: tt%.;:.. .               
              :8...8t%tt%SSS8:..%;.             
           ...: X@;:;t%%SXXXS;%.XX.8t           
          .S;tt8...:%%SSXXXX@tS:t:.8.::.        
       . .: SS:: :%t%SSX%X%SX%8X: ::  :         
       ;@ ;%;:  :%;SSXSSSt%%8%X...  @. ..       
      .8 X%:... .tSSXX%StX%;%%X@:   ;;...       
    ..:.:8   . @%SXXSXStt%@%%S;..:     X..      
     tt.t    .:.;XX@XS%X%:%%S;%t:8     %.8%     
   ... 8.     :t@@X@S%S%%StSt;;;..t     @.@:    
   ..: X     :.t@8@X%SSt%t%;;:tt...    .t.X:.   
   .:: @:    8 8@@XX%8%;;t;;:t::...%.   :.S:    
   ... 8t   :t%X@SSSS;;St;;:t::..@.S:.  :.t.    
   ... 8. . .@XX%X8%%S%;;:%:;.;.X:.8    %8X:    
   ..:@X@;. .XX@XSStStt;:%::...X:888t: .88S:    
      ; @t.;88@@%%tt:t:::t8@%S8:8.88@: S %%.    
     .t8%;::@SX%S%%;;:SX8t;;::::88888.t88%.     
     .:%t;:S8XSS%t8%%%8;:..    . @888888t       
      .;t:SXXSStttt;8....       ::S @88.        
       .:;;SS%t8SXtX.            %888@:         
        . 88%Xt%;X8S;:.   .:;%@8888;%8.         
        .::8S%t%;:....X8888.8.888% .;X%.        
         ..:S:8 t888888@8@S@8%;%;. .:@S.        
        . .X;;: :;; ... . .t:...    :::         
          8@;    .                              

                                      
                                      
for setting
http://jupiterstation.tech:8080/en/Projects/TR-560/tools

Change drivers > graphics > boot Logo > to 16 bit

continue(Y/n)?

EOF


echo ' \n'
    read -p  '>> ' yn
    case $yn in
        [Yy]* ) clear; break;;
        [Nn]* ) exit;;
        * )  clear ;  break;;
    esac
done

sudo apt install libncurses5-dev
make menuconfig


while true; do
 cat << "EOF"
 
Star Trek (1971 video game):
On or shortly after Unix epoch time.
 
quadrent      3/1 
 .  .  .  .  .  .  .  .  condition green                                                                        
 .  .  .  .  .  .  .  .                                                                        
 .  .  .  .  .  .  .  .                                                                        
 .  .  .  .  .  .  .  .                                                                      
 .  .  .  .  .  .  .  .       torpedows                                                                    
 .  .  .  .  .  .  .  .         energy                                                                   
 .  .  .  .  .  .  .  .        shields                                                                     
 .  .  .  .  .  .  .  .       klingons        

Command                                                              
                                                                                                  
Build kernel
continue(Y/n)?

EOF

    read -p  '>> ' yn
    case $yn in
        [Yy]* ) clear; break;;
        [Nn]* ) exit;;
        * )  clear ;  break;;
    esac
done
make -j4 zImage modules dtbs
sudo make modules_install
while true; do
 cat << "EOF"
 The Social ArtCasts                                                                                                   
MMMMMMMMMMMMMWX0OkxxddxxkkO0KXNWMMMMMMMMMMMMMMMM
MMMMMMMMMMWXko:,,,:cllllllc:::coxOXWMMMMMMMMMMMM
MMMMMMMMWXxc,,;lxOKNWWWWWWNX0kdc;,:dONMMMMMMMMMM
MMMMMMMW0l,,;o0NWWMMMMMMMMMMMMWN0d:,;o0WMMMMMMMM
MMMMMMM0c,,ckKK00KXNMMMMMWWMMMWWMWKo;,cOWMMMMMMM
MMMMMMNx,':OWXXXNK0KXXXXNXXNXXKXMMMXo,,lKMMMMMMM
MMMMMMXl,,dNMMMWNXK0000KXKKK000XWMMW0c';xWMMMMMM
MMMMMMKc,,xWWWN0kKXNNNNWWWWWWNNNNWWWNo,,dNMMMMMM
MMMMMMKc',oXNKOxkOO00OKK0KX0XX0O0XKXNd,,dNMMMMMM
MMMMMMXo,',o0XXNWNXNNXXXXXXKXNXXXNXNNo,,dNMMMMMM
MMMMMMWO:,',:d0XWMMMMMMMMMMMMMMMMMMMW0c,lKWMMMMM
MMMMMMMNx;'',,,coxk0XWMMMMMMMMMMMMMMMWKl,c0WMMMM
MMMMMMMMNkc,'',,'',,:oONWMMMMMMMMMMMMWXd,,:kNMMM
MMMMMMMMMWXOo;,,,'';ll:oOXMMMMMMMMMMMNd,,,ckNMMM
MMMMMMMMMMMMN0o;'',,o0kdd0MMMMMMMMMMM0c,'c0WMMMM
MMMMMMMMMMMMMMNd;,lxx0WNNWMMMMMMMMMMXd,',dNMMMMM
MMMMMMMMMMMMMMM0:,xNWWMMMMMMWWWWWMMWk;',c0WMMMMM
MMMMMMMMMMMMMMM0c:OWMMMMMN0xolloodxo:,';xWMMMMMM
MMMMMMMMMMMMMMWOlkNMMMW0xo;,;;:;;;,,'',lKMMMMMMM
MMMMMMMMMMMMMMW0KWMMWKd;,;lk0XXKKK0kxxkXWMMMMMMM
MMMMMMMMMMMMMMMMMMMWKl;lxONMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXdoONWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNKNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM                                                                
                                                                                                  
 Almost done copy files to /boot/

continue(Y/n)?

EOF

    read -p  '>> ' yn
    case $yn in
        [Yy]* ) clear; break;;
        [Nn]* ) exit;;
        * )  clear ;  break;;
    esac
done

sudo cp arch/arm/boot/dts/*.dtb /boot/
sudo cp arch/arm/boot/dts/overlays/*.dtb* /boot/overlays/
sudo cp arch/arm/boot/dts/overlays/README /boot/overlays/
sudo cp arch/arm/boot/zImage /boot/$KERNEL.img


```



# gpiozero
> "A simple interface to GPIO devices with Raspberry Pi, developed and maintained by Ben Nuttall and Dave Jones. "
> -gpiozero [readthedocs.io](https://gpiozero.readthedocs.io/en/stable/) 
## Installation
Install Raspbian stable 
```
sudo apt install python3-gpiozero
```
## Usage 
After installing visit
gpiozero - https://gpiozero.readthedocs.io/en/stable/recipes.html
Lots of examples and documentation.

The following is one such.
```
pinout
```
Prints out system board info: 
```
.-------------------------.
| oooooooooooooooooooo J8 |
| 1ooooooooooooooooooo   |c
---+       +---+ PiZero W|s
 sd|       |SoC|   V1.1  |i
---+|hdmi| +---+  usb pwr |
`---|    |--------| |-| |-'

Revision           : 9000c1
SoC                : BCM2835
RAM                : 512MB
Storage            : MicroSD
USB ports          : 1 (of which 0 USB3)
Ethernet ports     : 0 (0Mbps max. speed)
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 0

J8:
   3V3  (1) (2)  5V
 GPIO2  (3) (4)  5V
 GPIO3  (5) (6)  GND
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8
   GND (25) (26) GPIO7
 GPIO0 (27) (28) GPIO1
 GPIO5 (29) (30) GND
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

For further information, please refer to https://pinout.xyz/
```
 
[GitHub](http://github.com/Tearran/)

> "Failures are steps we must take make to achieve success"
> -The Traveling Aspie

### Thanks and refrences
- https://www.raspberrypi.com/documentation/
- https://www.kernel.org/
- https://readthedocs.io

