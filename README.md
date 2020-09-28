# RemoveBG-GIMP
A small plugin to easily remove the Background of a Image using https://www.remove.bg/

## Installation:
### Windows: 
requires `requests`, which can be obtained with `pip install requests` (which requires python)

Just put the file in your plugins- directory:

C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins

### Linux: 
#### see branch:linux



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
