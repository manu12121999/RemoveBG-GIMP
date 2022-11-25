# RemoveBG-GIMP
A small plugin to easily remove the background of an image using https://www.remove.bg/


## THIS BRANCH WORKS ONLY FOR GIMP >= 2.99. STILL IN DEVELOPMENT

## Usage
1. Install the plugin as shown below
2. Filters → RemoveBackground → Remove Background
3. Enter your key in the key dialog. You get a API key for free at https://www.remove.bg/api
![1](https://user-images.githubusercontent.com/66686353/117555656-59369e00-b061-11eb-870e-1223874372ed.png)
![2](https://user-images.githubusercontent.com/66686353/204058389-d9adfa03-b35f-4685-a025-5570b4412210.png)
![3](https://user-images.githubusercontent.com/66686353/117555657-59cf3480-b061-11eb-985c-fe187edb162c.png)

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
## Notes:
- In Gimp 2.99 new plugins do not get queried if they are not placed inside a subfolder. 

## Licence:
It is not an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!

