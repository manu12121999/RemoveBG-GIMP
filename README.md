# RemoveBG-GIMP
A small plugin to easily remove the Background of an image using https://www.remove.bg/. 

## Installation:
### Windows: 
1. Install python

2. Install  `requests` with `pip install requests`

3. Put the remove_background.py file in your plugins- directory:

C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

#### if the plugin does not show up, open a command prompt as admin and type:
```
cd 'C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins\' 
python -m pip install --user virtualenv
python -m virtualenv gimpenv
source gimpenv/bin/activate
python -m pip install requests
deactivate
 ```

### Linux: 
1. Install python and requests ( `pip install requests`)

2. Search your plugins- directory. The directory might be at

 ~/.gimp-2.10/plug-ins/

 or /usr/lib/gimp/2.0/plug-ins  

3. Put the remove_background.py in this directory and make it executable with `chmod +x remove_background.py` 

#### if the plugin does not show up in Gimp, then run (in your plugins directory):

```
chmod +x remove_background.py
python -m pip install --user virtualenv
python -m virtualenv gimpenv
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
- if removebackground does not show up in the GIMP Menu, it's because requests is not found. 
If requests is installed correctly, tell me about it in the Issue Section.

## Notes:
* for convenience, hard-code your key in the request-part of the code
* This branch works only for GIMP up to 2.10. For new versions of Gimp (2.99 or 3.0), check out the branch "gimp3.0".

## Licence:
It is not a official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
