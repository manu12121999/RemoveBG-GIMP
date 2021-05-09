#!/usr/bin/env python
import os 
baseLoc = os.path.dirname(os.path.realpath(__file__))+'/'

from gimpfu import *
import tempfile
import sys
from sys import platform

sys.path.extend([baseLoc+'gimpenv/lib/python2.7', baseLoc+'gimpenv/lib/python2.7/site-packages', baseLoc+'gimpenv/lib/python2.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.6', baseLoc+'gimpenv/lib/python3.6/site-packages', baseLoc+'gimpenv/lib/python3.6/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.7', baseLoc+'gimpenv/lib/python3.7/site-packages', baseLoc+'gimpenv/lib/python3.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.8', baseLoc+'gimpenv/lib/python3.8/site-packages', baseLoc+'gimpenv/lib/python3.8/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.9', baseLoc+'gimpenv/lib/python3.9/site-packages', baseLoc+'gimpenv/lib/python3.9/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/Lib', baseLoc+'gimpenv/Lib/site-packages', baseLoc+'gimpenv/Lib/site-packages/setuptools'])
import requests



def remove_background(image, layer, key):
    pdb.gimp_image_undo_group_start(image)
    

    #input
    height = pdb.gimp_drawable_height(layer)
    width = pdb.gimp_drawable_width(layer)
    
    new_height = float(height)
    new_width = float(width)
    
    if new_height > 1080.0:   #scale down 
        factor = new_height/1080.0
        new_height = 1080
        new_width = int(new_width / factor)

    if new_width > 1920.0:
        factor = new_width/1920.0
        new_width = 1920
        new_height = int(new_height/factor)
    
    

    layer_copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image,layer_copy,None,0)
    pdb.gimp_layer_scale(layer_copy, new_width, new_height, 0)  #make a copy and scale it down
    
    temp = tempfile.gettempdir()
    if platform == "linux" or platform == "linux2":
        f = "/tmp/temp.png"
        f2 =  "/tmp/temp2.png"
    else:
        f = temp + "\\temp.png"
        f2 = temp + "\\temp2.png"
    
    pdb.file_png_save_defaults(image, layer_copy, f, f)
    
    pdb.gimp_image_remove_layer(image, layer_copy)
    
    
    #remove.bg
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(f,'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': key},     #HARD CODE YOUR KEY HERE e.g: {'X-Api-Key' ="asdfjas"},
    )
    if response.status_code == requests.codes.ok:
    	with open(f2, 'wb') as out:
            out.write(response.content)
    	#output
    	outlayer = pdb.gimp_file_load_layer(image, f2)
    	pdb.gimp_image_insert_layer(image, outlayer, None, 0) # because you cant scale without adding the layer


    	pdb.gimp_layer_scale(outlayer, width, height, 0)
    	#pdb.gimp_layer_resize(outlayer, width, height, 0, 0)

    	mask = pdb.gimp_layer_create_mask(outlayer, 2)
    	pdb.gimp_layer_add_mask(layer, mask)
    	pdb.gimp_image_remove_layer(image, outlayer)

    	pdb.gimp_image_undo_group_end(image)

    else:
    	pdb.gimp_image_undo_group_end(image)
        print("Error:", response.status_code, response.text)
    

register(
    "python-fu-remove_background",
    "Easy Way to remove the BG of a Picture",
    "Description.",
    "Manuel V.", "M", "2020",
    "remove_background",
    "*", 
    [
        (PF_IMAGE, "image","takes current image", None),
        (PF_DRAWABLE, "drawable","input layer", None),
        (PF_STRING, "key", "Remove_bg KEY", "INSERT_YOUR_KEY_HERE")

    ],
    [],
    remove_background, menu="<Image>/Filters")

main()
