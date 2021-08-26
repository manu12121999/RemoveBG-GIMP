# RemoveBG-GIMP
This plugin automatically removes the image background using https://www.remove.bg/. The website uses neuronal networks to distinguish the foreground from the background. After that a layer mask is applied to the image which can be edited to improve the cut-out, if needed. 


## Usage
1. Install the Plugin as shown in the installation section
2. Filters -> removeBackground
3. Insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (112)](https://user-images.githubusercontent.com/66686353/84803152-e1532580-b001-11ea-9bf5-ff2061c3f061.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)


## Installation
### Windows: 
1. Put the remove_background.py file in your plugins- directory:

* C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

2. Install requests for GIMPs python (in a command prompt, as an admin) with

```
cd "C:\Program Files\GIMP 2\bin\"
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python.exe get-pip.py
python.exe -m pip install requests
```

3. restart GIMP

#### if the plugin does not show up proceed with the following
1. Install python
2. Type the following commands in a command prompt run as an admin:

```
cd "C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins\" 
python -m venv gimpenv
gimpenv\Scripts\activate.bat
python -m pip install requests
deactivate
 ```
 
### Linux: 
1. Install python

2. Search your plugins- directory. The directory might be at

 ~/.gimp-2.10/plug-ins/

 ~/.config/GIMP/2.10/plug-ins

 or /usr/lib/gimp/2.0/plug-ins  

3. Put the remove_background.py in this directory and make it executable with `chmod +x remove_background.py` 

4. Install requests:
```
chmod +x remove_background.py
python3 -m venv gimpenv
source gimpenv/bin/activate
python3 -m pip install requests
deactivate
```
5. Make sure you have installed python support for gimp. (`gimp-python` package for ubuntu or `python2-gimp` from the AUR)
 

## Problems:
- if removebackground does not show up in the GIMP Menu, it's because requests is not found. 
If requests is installed correctly, tell me about it in the Issue Section.

## Notes:
* The plugin uploads the image to the website remove.bg. Don't use it for anything confidential!
* hard-code your key in the code for more convince
* This branch works only for GIMP up to 2.10. For new versions of Gimp (2.99 or 3.0), check out the branch "gimp3.0".

## Licence:
It is not a official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
