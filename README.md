# RemoveBG-GIMP
A small plugin to easily remove the background of an image using https://www.remove.bg/


## Installation:
1. Use `remove_bg_gimp2.py` if you have GIMP up to 2.10 and `remove_bg_gimp3.py` for GIMP 3.0 or higher.

2. Put the python file inside GIMP's plugin-directory. It is important, that the `.py` file is placed inside a folder with the same name as the file (except the `.py` ending). E.g. `...\gimp\3.0\plug-ins\remove_bg_gimp3\remove_bg_gimp3.py`

    The pugin directory can be e.g. at `C:\Program Files\GIMP 3\lib\gimp\3.0\plug-ins\` or `C:\Users\<USERNAME>\AppData\Roaming\GIMP\3.0\plug-ins\` If you cant find it, go inside GIMP to `Edit->Preferences->Folders->Plugins`

3. On Linux, make the file executable (`chmod +x remove_bg_gimp3.py`) and make sure you have installed python support for gimp. (`gimp-python` package for ubuntu or `python2-gimp` from the AUR)


## Usage
1. Install the plugin as shown above
2. Filters → RemoveBackground → Remove Background
3. Enter your key in the key dialog. You get a API key for free at https://www.remove.bg/api
4. Press `Save Settings` to save the key for next uses
![1](https://user-images.githubusercontent.com/66686353/117555656-59369e00-b061-11eb-870e-1223874372ed.png)
![2](https://user-images.githubusercontent.com/66686353/204058389-d9adfa03-b35f-4685-a025-5570b4412210.png)
![3](https://user-images.githubusercontent.com/66686353/117555657-59cf3480-b061-11eb-985c-fe187edb162c.png)


## Notes:
* The plugin uploads the image to the website remove.bg. Don't use it for anything confidential!
* If encountering any problems, try out the gimp2.0/requests branch, which uses more advanced libraries, although it takes extra steps to install.

## Licence:
It is **not** an official remove.bg plugin, so keep their Terms of Service in mind (https://www.remove.bg/tos)

Besides that, you can do whatever you want with my code!
