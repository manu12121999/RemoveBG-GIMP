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
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import gettext
import os, sys


baseLoc = os.path.dirname(os.path.realpath(__file__))+'/'
sys.path.extend([baseLoc+'gimpenv/lib/python2.7', baseLoc+'gimpenv/lib/python2.7/site-packages', baseLoc+'gimpenv/lib/python2.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.6', baseLoc+'gimpenv/lib/python3.6/site-packages', baseLoc+'gimpenv/lib/python3.6/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.7', baseLoc+'gimpenv/lib/python3.7/site-packages', baseLoc+'gimpenv/lib/python3.7/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.8', baseLoc+'gimpenv/lib/python3.8/site-packages', baseLoc+'gimpenv/lib/python3.8/site-packages/setuptools'])
sys.path.extend([baseLoc+'gimpenv/lib/python3.9', baseLoc+'gimpenv/lib/python3.9/site-packages', baseLoc+'gimpenv/lib/python3.9/site-packages/setuptools'])

sys.path.extend([baseLoc+'gimpenv/Lib', baseLoc+'gimpenv/Lib/site-packages', baseLoc+'gimpenv/Lib/site-packages/setuptools'])
import requests

_ = gettext.gettext
def N_(message): return message

class RemoveBG(Gimp.PlugIn):

    ## Parameters ##
    __gproperties__ = {
        "key": (str,
                 "Key",
                 "key",
                 "TYPE YOUR KEY FROM remove.bg HERE",
                 GObject.ParamFlags.READWRITE),
    }
       
    ## GimpPlugIn virtual methods ##
    def do_query_procedures(self):
        self.set_translation_domain("gimp30-python",
                                    Gio.file_new_for_path(Gimp.locale_directory()))

        return [ 'python-fu-remove-background' ]


    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.plug_in_remove_bg, None)
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
        
        procedure.add_argument_from_property(self, "key")

        return procedure
        
   
    #plugin-in implementation
    def plug_in_remove_bg(self, procedure, run_mode, image, n_layers, layers, args, data):
        config = procedure.create_config()
        config.begin_run(image, run_mode, args)
        
        if run_mode == Gimp.RunMode.INTERACTIVE:
            GimpUi.init('python-fu-remove-bg')
            dialog = GimpUi.ProcedureDialog.new(procedure, config)
            dialog.fill(None)
            if not dialog.run():
                dialog.destroy()
                config.end_run(Gimp.PDBStatusType.CANCEL)
                return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())
   
        key = config.get_property('key')
        Gimp.context_push()
        
        image.undo_group_start()

        #input
        height = layers[0].get_height()
        width =  layers[0].get_width ()
        
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
        
        
        layer_copy = layers[0].copy()
        image.insert_layer(layer_copy, None, 1)
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
            

            image.insert_layer(result_layer, None, 1) # because you cant scale without adding the layer

            result_layer.scale(width, height, 0)

            mask = result_layer.create_mask(2)
            layers[0].add_mask(mask)
            image.remove_layer(result_layer)
            image.undo_group_end()
            
            #cleanup
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            file1.delete()
            file2.delete()
            config.end_run(Gimp.PDBStatusType.SUCCESS)
            Gimp.displays_flush()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

        else: #false key
            image.undo_group_end()
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            print("Error:", response.status_code, response.text)
            
            #clean_up
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            file1.delete()
            file2.delete()
            config.end_run(Gimp.PDBStatusType.SUCCESS)
            Gimp.displays_flush()
            return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())
                    
        

Gimp.main(RemoveBG.__gtype__, sys.argv)
