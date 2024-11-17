#!/usr/bin/env python3

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

import time
import sys
import os
import urllib.request
import urllib.error
import ssl


# This Plugin is only for GIMP Version 3
class RemoveBG(Gimp.PlugIn):

    ## GimpPlugIn virtual methods ##
    def do_query_procedures(self):
        return [ 'remove-background' ]


    def do_create_procedure(self, name):
        Gegl.init(None)
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.plug_in_remove_bg, None)
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.ALWAYS)
        procedure.set_documentation("Easy way to remove any background from an image",
                                    "Easy way to remove any background from an image",
                                    name)
        procedure.set_menu_label("Remove Background")
        procedure.set_attribution("Manuel Vogel",
                                  "Manuel Vogel",
                                  "2020-2024")
        procedure.add_menu_path("<Image>/Filters/Remove_BG/")

        # procedure.add_argument_from_property(self, "key")

        procedure.add_string_argument("key", "KEY from remove.bg. Get it for free: https://www.remove.bg/api  ", "KEY from remove.bg",
                                      "Insert HERE", GObject.ParamFlags.READWRITE)
        procedure.add_boolean_argument("consent", "REQUIRED: I am aware that my image will be processed by remove.bg", "consent",
                                       False, GObject.ParamFlags.READWRITE)
        return procedure


    def call_api(self, key, input_file, output_file):
        # remove.bg API URL
        url = "https://api.remove.bg/v1.0/removebg"
        headers = {"X-Api-Key": key}

        # Boundary for multipart form-data
        boundary = "jsdjfhsaasdfadflfhahfhj"
        part_boundary = '--' + boundary

        # Read the image content
        if not os.path.exists(input_file):
            print(f"File not found: {input_file}")
        with open(input_file, "rb") as f:
            image_content = f.read()

        # Construct the body with multipart form-data
        part_list = [
            part_boundary,
            'Content-Disposition: form-data; name="image_file"; filename="a.png"',
            'Content-Type: image/png',
            '',
            image_content,
            '--' + boundary + '--',
            ''
        ]

        # Join parts with "\r\n" and ensure it's a byte string
        body = b'\r\n'.join(part.encode('utf-8') if isinstance(part, str) else part for part in part_list)

        # Prepare the request
        req = urllib.request.Request(url, data=body, headers=headers)
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
        req.add_header('Content-length', str(len(body)))

        # Create an SSL context to ignore certificate verification
        context = ssl._create_unverified_context()

        # Make the request and read the response
        try:
            with urllib.request.urlopen(req, context=context) as response:
                response_data = response.read()

            # Write the response to an output file
            with open(output_file, "wb") as out:
                out.write(response_data)
        except urllib.error.HTTPError:
            return False

        return True

    def call_api_requests(self, key, input_file, output_file):
        # remove.bg
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
             files={'image_file': open(input_file.peek_path(), 'rb')},
             data={'size': 'auto'},
             headers={'X-Api-Key': key},
         )
        if response.status_code == requests.codes.ok:
            with open(output_file.peek_path(), 'wb') as out:
                out.write(response.content)
            return True
        else:
            return False

    @staticmethod
    def try_deleting(file):
        try:
            file.delete()
        except gi.repository.GLib.GError:
            pass

    # plugin-in implementation
    def plug_in_remove_bg(self, procedure, run_mode, image, layers, config, data):
        if run_mode == Gimp.RunMode.INTERACTIVE:
            GimpUi.init('python-fu-remove-bg')
            dialog = GimpUi.ProcedureDialog.new(procedure, config)
            dialog.fill(None)
            if not dialog.run():
                dialog.destroy()
                return procedure.new_return_values(Gimp.PDBStatusType.CANCEL, GLib.Error())

        key = config.get_property('key')
        consent = config.get_property('consent')
        if not consent:
            return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, GLib.Error(message="Please agree to the usage of this plugin"))
        Gimp.context_push()

        image.undo_group_start()

        # input
        height = layers[0].get_height()
        width =  layers[0].get_width()

        new_height = float(height)
        new_width = float(width)

        if new_height > 1080.0:  # scale down
            factor = new_height/1080.0
            new_height = 1080
            new_width = int(new_width / factor)

        if new_width > 1920.0:
            factor = new_width/1920.0
            new_width = 1920
            new_height = int(new_height/factor)

        layer_copy = layers[0].copy()
        image.insert_layer(layer_copy, None, 1)
        layer_copy.scale(new_width, new_height, 0)  # make a copy and scale it down

        file1 = Gimp.temp_file('png')
        file2 = Gimp.temp_file('png')

        # Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, [layer_copy], GFile(file1))
        s = Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, file1, None)  # image.get_selected_drawables()
        if not s:
            print("FAILED TO SAVE")

        image.remove_layer(layer_copy)

        # remove.bg
        success = self.call_api(key, file1.get_path(), file2.get_path())

        if success:
            # output
            result_layer = Gimp.file_load_layer(Gimp.RunMode.NONINTERACTIVE, image, file2)

            # insert layer because you cannot scale without adding the layer
            image.insert_layer(result_layer, None, 1)

            result_layer.scale(width, height, 0)

            mask = result_layer.create_mask(2)
            layers[0].add_mask(mask)
            image.remove_layer(result_layer)

            image.undo_group_end()

            # cleanup
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            self.try_deleting(file1)
            self.try_deleting(file2)
            # config.end_run(Gimp.PDBStatusType.SUCCESS)
            Gimp.displays_flush()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

        else:  # wrong key
            image.undo_group_end()

            # clean_up
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            self.try_deleting(file1)
            self.try_deleting(file2)
            # config.end_run(Gimp.PDBStatusType.SUCCESS)
            Gimp.displays_flush()
            return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, GLib.Error(message="Key not correct"))

Gimp.main(RemoveBG.__gtype__, sys.argv)
