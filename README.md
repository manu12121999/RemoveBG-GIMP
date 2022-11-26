# RemoveBG-GIMP
This plugin automatically removes the image background using https://www.remove.bg/. The website uses neuronal networks to distinguish the foreground from the background. After that, a layer mask is applied to the image, which can be edited to improve the cut-out, if needed. 

## This branch uses the python package ```requests``` which has to be installed seperately.

## Usage
1. Install the Plugin as shown in the installation section
2. Filters -> removebackground
3. Insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![1](https://user-images.githubusercontent.com/66686353/117555656-59369e00-b061-11eb-870e-1223874372ed.png)


## Installation
### Windows: 
1. Put the remove_background.py file in your plugins directory:

* C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

2. Install _requests_ for GIMP's python (in a command prompt, as an admin) with:

```
cd "C:\Program Files\GIMP 2\bin\"
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python.exe get-pip.py
python.exe -m pip install requests
```

3. restart GIMP

#### if the plugin does not show up, proceed with the following:
1. Install python
2. Type the following commands in a command prompt, run as an admin:

```
cd "C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins\" 
python -m venv gimpenv
gimpenv\Scripts\activate.bat
python -m pip install requests
deactivate
 ```
 
### Linux: 
1. Install python

2. Search your plugins directory. The directory might be at:

 ~/.gimp-2.10/plug-ins/

 ~/.config/GIMP/2.10/plug-ins

 or /usr/lib/gimp/2.0/plug-ins  

3. Put _remove_background.py_ in this directory and make it executable with `chmod +x remove_background.py` 

4. Install _requests_:
```
chmod +x remove_background.py
python3 -m venv gimpenv
source gimpenv/bin/activate
python3 -m pip install requests
deactivate
```
5. Make sure you have installed python support for gimp. (`gimp-python` package for ubuntu or `python2-gimp` from the AUR)
 

## Problems:
* if removebackground does not show up in the GIMP menu, it's because _requests_ is not found. 
If _requests_ is installed correctly, let me know about it in the Issues section.

## Notes:
* The plugin uploads the image to the website remove.bg. Don't use it for anything confidential!
* Hard-code your key in the code for more convenience
* This branch works only for GIMP up to version 2.10. For newer versions of GIMP (2.99 or 3.0), check out the branch "gimp3.0".

## Licence:
It is **not** an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
