# RemoveBG-GIMP
A small plugin to easily remove the Background of a Image using https://www.remove.bg/

## Installation:
### Windows: 
1. Install python 2.7 and pip

2. Install  `requests` with `pip install requests`

3. Put the file in your plugins- directory:

C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

### Linux: 
1.Install python 2.7 and pip

2. Search your plugins- directory. The directory might be at

~/.gimp-2.10/plug-ins/

or /usr/lib/gimp/2.0/plug-ins  

or ~/snap/gimp/281/.config/GIMP/2.10/plug-ins

#### 3.Put the plugin in this directory and run in the same directory:

```
chmod +x remove_background.py
python -m pip install --user virtualenv
python -m virtualenv gimpenv
source gimpenv/bin/activate
python -m install requests
deactivate
```
 
 or execute the setup file


## Usage:
1. Filters -> removeBackground
2. insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (112)](https://user-images.githubusercontent.com/66686353/84803152-e1532580-b001-11ea-9bf5-ff2061c3f061.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)

## Problems:
- if removebackground does not show up in the GIMP Menu, it's because requests is not found. 
If requests is installed correctly, tell me about it in the Issue Section.
- for some linux systmems the master branch works fine. If it does not work, check out the linux branch. 

## Notes:
for convenience, hard-code your key in the request-part of the code
