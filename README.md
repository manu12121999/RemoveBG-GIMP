# RemoveBG-GIMP
A small plugin to easily remove the background of an image using https://www.remove.bg/


## THIS BRANCH WORKS ONLY FOR GIMP >= 2.99. Still in DEVELOPMENT, so expect CRASHES

## Installation:
### Windows: 
1. Install python

2. Put the remove_background folder(unzipped) in your plugin-directory at *C:\Program Files\GIMP 2.99\lib\gimp\2.99\plug-ins*

3. Install requests for the python installation of Gimp by opening the command prompt in admin mode and type: (replace remove_bg by the name of the folder)
```
 cd C:\Program Files\GIMP 2.99\lib\gimp\2.99\plug-ins\remove_bg   
 python -m venv gimpenv
 gimpenv\Scripts\activate.bat
 python -m pip install requests
 deactivate
```

### Linux: 
1. Install python

2. Search your plugins- directory. You can find this directory in the GIMP Preferences. 

3. Put the remove_background directory there (unzipped).

4. make it executable and install requests with: 

```
chmod +x remove_background.py
python3 -m venv gimpenv
source gimpenv/bin/activate
python3 -m pip install requests
deactivate
```
 

## Usage:
1. Filters → RemoveBackground → removeBackground
2. Enter your key in the key dialog. You get a API key for free at https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)

## Notes:
- In Gimp 2.99 new plugins do not get queried if they are not placed inside a subfolder. 

## Licence:
It is not an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
