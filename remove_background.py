#!/usr/bin/env python3

# This Plugin is for GIMP Version >= 2.99
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
gi.require_version('Gegl', '0.4')
from gi.repository import Gegl
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gio

import gettext
_ = gettext.gettext

import os, sys


baseLoc = os.path.dirname(os.path.realpath(__file__))+'/'
sys.path.extend([baseLoc+'gimpenv/lib/python2.7', baseLoc+'gimpenv/lib/python2.7/site-packages', baseLoc+'gimpenv/lib/python2.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.6', baseLoc+'gimpenv/lib/python3.6/site-packages', baseLoc+'gimpenv/lib/python3.6/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.7', baseLoc+'gimpenv/lib/python3.7/site-packages', baseLoc+'gimpenv/lib/python3.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.8', baseLoc+'gimpenv/lib/python3.8/site-packages', baseLoc+'gimpenv/lib/python3.8/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.9', baseLoc+'gimpenv/lib/python3.9/site-packages', baseLoc+'gimpenv/lib/python3.9/site-packages/setuptools'])

sys.path.extend([baseLoc+'gimpenv/Lib', baseLoc+'gimpenv/Lib/site-packages', baseLoc+'gimpenv/Lib/site-packages/setuptools'])
import requests

def N_(message): return message



def remove_bg(procedure, run_mode, image, drawable, args, data):
    with open(os.path.dirname(os.path.realpath(__file__))+'/key.txt','r') as key_file:
       key = key_file.read()
    image.undo_group_start()

    #input
    height = drawable.height()
    width =  drawable.width ()
    
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
    
    
    layer_copy = drawable.copy()
    image.insert_layer(layer_copy,None,0)
    layer_copy.scale(new_width, new_height, 0)  #make a copy and scale it down
    
    file1 = Gimp.temp_file('png')
    file2 = Gimp.temp_file('png')
 
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE,image,[layer_copy],file1)

    image.remove_layer(layer_copy)
    
    
    #remove.bg
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
         files={'image_file': open(file1.peek_path(),'rb')},
         data={'size': 'auto'},
         headers={'X-Api-Key': key},
     )
    if response.status_code == requests.codes.ok:
        with open(file2.peek_path(), 'wb') as out:
            out.write(response.content)
        #output
        result_layer = Gimp.file_load_layer(Gimp.RunMode.NONINTERACTIVE,image,file2)
        

        image.insert_layer(result_layer, None, 0) # because you cant scale without adding the layer


        result_layer.scale(width, height, 0)
        #Gimp.gimp_layer_resize(result_layer, width, height, 0, 0)

        mask = result_layer.create_mask(2)
        drawable.add_mask(mask)
        image.remove_layer(result_layer)
        image.undo_group_end()

    else:
        image.undo_group_end()
        print("Error:", response.status_code, response.text)
        
    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())



class RemoveBG(Gimp.PlugIn):

    ## GimpPlugIn virtual methods ##
    def do_query_procedures(self):
        self.set_translation_domain("gimp30-python",
                                    Gio.file_new_for_path(Gimp.locale_directory()))

        return [ 'python-fu-remove-background' ]


    def do_create_procedure(self, name):
        procedure = None
        if name == 'python-fu-remove-background':
            procedure = Gimp.ImageProcedure.new(self, name,
                                                Gimp.PDBProcType.PLUGIN,
                                                remove_bg, None)
            procedure.set_image_types("*")
            procedure.set_documentation(
                N_("Easy way to remove any background from an image"),
                "test",  
                name)
            procedure.set_menu_label(N_("Remove Backgound"))
            procedure.set_attribution("Manuel Vogel",
                                      "Manuel Vogel",
                                      "2020")
            procedure.add_menu_path("<Image>/Filters/RemoveBackgound")

        return procedure
        
 

Gimp.main(RemoveBG.__gtype__, sys.argv)
