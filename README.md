# RemoveBG-GIMP
A small plugin to easily remove the Background of a Image with remove.bg

## Installation:
requires `requests`, which can be obtained with `pip install requests` (which requires python)

Just put the file in your plugins- directory:
### Windows: 
C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins
### Linux
Might not work ( ImportError: no modue named requests) even when requests is installed. I will look into it later. If it works, the directory might be at

~/.gimp-2.10/plug-ins/

or /usr/lib/gimp/2.0/plug-ins

 `chmod +x ~/.gimp-2.10/plug-ins/remove_background.py`

## Usage:
1. Filters -> removeBackground
2. insert your RemoveBG API Key, which you can get from https://www.remove.bg/api
![Screenshot (111)](https://user-images.githubusercontent.com/66686353/84802853-773a8080-b001-11ea-9c1a-5da90977a010.png)
![Screenshot (112)](https://user-images.githubusercontent.com/66686353/84803152-e1532580-b001-11ea-9bf5-ff2061c3f061.png)
![Screenshot (113)](https://user-images.githubusercontent.com/66686353/84802857-786bad80-b001-11ea-9bdd-be2c37bbea8d.png)

## Problems:
- does only work on Windows properly 
- it might currently only work on Linux(Ubuntu) with the GIMP you get from `sudo apt install gimp` , but not with the one you get from `sudo snap install gimp`
- with Linux, change f and f2 to 
    `f = "/tmp/temp.png"`
    `f2 =  "/tmp/temp2.png"`
- hasn't been tested much

## Notes:
for convenience, hard-code your key in the request-part of the code
