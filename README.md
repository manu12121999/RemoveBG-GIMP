# RemoveBG-GIMP
This plugin automatically removes the image background using https://www.remove.bg/. The website uses neuronal networks to distinguish the foreground from the background. After that, a layer mask is applied to the image, which can be edited to improve the cut-out, if needed. 


## Usage
1. Install the plugin as shown in the installation section
2. Filters → removebackground
3. Insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![1](https://user-images.githubusercontent.com/66686353/117555656-59369e00-b061-11eb-870e-1223874372ed.png)

![2](https://user-images.githubusercontent.com/66686353/204058389-d9adfa03-b35f-4685-a025-5570b4412210.png)

![3](https://user-images.githubusercontent.com/66686353/117555657-59cf3480-b061-11eb-985c-fe187edb162c.png)


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
* If encountering any problems, try out the gimp2.0/requests branch, which uses more advanced libraries, although it takes extra steps to install.

## Notes:
* The plugin uploads the image to the website remove.bg. Don't use it for anything confidential!
* Hard-code your key in the code for more convenience
* This branch works only for GIMP up to version 2.10. For newer versions of GIMP (2.99 or 3.0), check out the branch "gimp3.0".

## Licence:
It is **not** an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
