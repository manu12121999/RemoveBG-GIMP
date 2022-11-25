# RemoveBG-GIMP
This plugin automatically removes the image background using https://www.remove.bg/. The website uses neuronal networks to distinguish the foreground from the background. After that, a layer mask is applied to the image, which can be edited to improve the cut-out, if needed. 


## Usage
1. Install the Plugin as shown in the installation section
2. Filters -> removebackground
3. Insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (112)](https://user-images.githubusercontent.com/66686353/84803152-e1532580-b001-11ea-9bf5-ff2061c3f061.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)


## Installation
### Windows: 
1. Put the remove_background.py file in your plugins directory:

* C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

2. restart GIMP
 
### Linux: 
1. Search your plugins directory. The directory might be at:

 ~/.gimp-2.10/plug-ins/

 ~/.config/GIMP/2.10/plug-ins

 or /usr/lib/gimp/2.0/plug-ins  

3. Put _remove_background.py_ in this directory and make it executable with `chmod +x remove_background.py` 

4. Make sure you have installed python support for gimp. (`gimp-python` package for ubuntu or `python2-gimp` from the AUR)
 

## Problems:
* If encourerning any problems, try out the gimp2.0/requests branch, which uses much libraries, altough it takes extra steps to install.

## Notes:
* The plugin uploads the image to the website remove.bg. Don't use it for anything confidential!
* Hard-code your key in the code for more convenience
* This branch works only for GIMP up to version 2.10. For newer versions of GIMP (2.99 or 3.0), check out the branch "gimp3.0".

## Licence:
It is **not** an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
