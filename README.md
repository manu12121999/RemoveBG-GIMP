## THIS BRANCH WORKS ONLY FOR GIMP >= 2.99. 
Currently in development

# RemoveBG-GIMP
A small plugin to easily remove the Background of a Image using https://www.remove.bg/

## Installation:
### Windows: 
1. Install python

2. Put the remove_background folder(unzipped) in a your plugins- directory (at C:\Program Files\GIMP 2.99\lib\gimp\2.99\plug-ins)

3. Install requests in for the pyhton installation of Gimp by opening the command prompt in admin mode and typ something like
```
 cd C:\Program Files\GIMP 2.99\lib\gimp\2.99\plug-ins\remove_bg   
 python -m venv gimpenv
 gimpenv\Scripts\activate.bat
 python -m pip install requests
 deactivate
```

### Linux: 
1. Install python

2. Search your plugins- directory. The directory might be at:

 *~/.gimp-2.10/plug-ins/*        
 */usr/lib/gimp/2.0/plug-ins*      
 *~/snap/gimp/281/.config/GIMP/2.10/plug-ins*

3. Put the remove_background folder in this directory

4. make it executable and install requests with: 

```
chmod +x remove_background.py
python -m venv gimpenv
source gimpenv/bin/activate
python -m pip install requests
deactivate
```
 

## Usage:
1. Filters -> removeBackground
2. insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (112)](https://user-images.githubusercontent.com/66686353/84803152-e1532580-b001-11ea-9bf5-ff2061c3f061.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)

## Problems:
- You might need to hard Code your key in the Code, if there is not dialog.


## Licence:
It is not a official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
