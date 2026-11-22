# RemoveBG-GIMP
A small plugin to easily remove the background of an image using REST endpoints (such as  `remove.bg`, `bgclear.ai`, `cutmatte.com`, or a custom endpoint)

Note that `remove.bg` is shutting down its standalone API on December 1, 2026). Replace it with another endpoint (new API key required) or use the fully local [background removal plugin](https://github.com/manu12121999/GIMP-Background-Remover)

## Installation:
1. Locate GIMP's plugin directory. 
    common paths include `~/.config/GIMP/3.2/plug-ins`, `C:\Program Files\GIMP 3\lib\gimp\3.2\plug-ins\` or `C:\Users\<USERNAME>\AppData\Roaming\GIMP\3.2\plug-ins\` 
    If you cant find it, go inside GIMP to `Edit->Preferences->Folders->Plugins`

2. Put the python file inside GIMP's plugin-directory. It is important, that the `.py` file is placed inside a folder with the same name as the file (except the `.py` ending). E.g. `...\gimp\3.0\plug-ins\remove_bg\remove_bg.py`

3. On Linux, make the file executable (`chmod +x remove_bg.py`)

4. Restart GIMP


## Usage
1. Install the plugin as shown above
2. Filters → Remove_BG → Remove Background
3. Choose the url and enter your key in the key dialog. You get a API key for free at the respected websites
4. Press `Save Settings` to save the key for next uses
![1](https://user-images.githubusercontent.com/66686353/117555656-59369e00-b061-11eb-870e-1223874372ed.png)
![2](https://user-images.githubusercontent.com/66686353/204058389-d9adfa03-b35f-4685-a025-5570b4412210.png)
![3](https://user-images.githubusercontent.com/66686353/117555657-59cf3480-b061-11eb-985c-fe187edb162c.png)


## Notes:
* The plugin uploads the image to be processed by the website. Don't use it for anything confidential!

## Licence:
Please follow the Terms of Service of whichever API endpoint you use.

Besides that, you can do whatever you want with my code!

