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

import os
import sys
import urllib.request
import urllib.error
import ssl


PRESET_URLS = {
    "cutmatte": "https://api.cutmatte.com/v1.0/removebg",
    "bgclear": "https://www.bgclear.ai/api/v1/remove",
    "remove_bg": "https://api.remove.bg/v1.0/removebg",
}


# This Plugin is only for GIMP Version 3
class RemoveBG(Gimp.PlugIn):

    ## GimpPlugIn virtual methods ##
    def do_query_procedures(self):
        return ['remove-background']

    def do_create_procedure(self, name):
        Gegl.init(None)
        procedure = Gimp.ImageProcedure.new(
            self,
            name,
            Gimp.PDBProcType.PLUGIN,
            self.plug_in_remove_bg,
            None,
        )
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.ALWAYS)
        procedure.set_documentation(
            "Easy way to remove any background from an image",
            "Easy way to remove any background from an image",
            name,
        )
        procedure.set_menu_label("Remove Background")
        procedure.set_attribution("Manuel Vogel", "Manuel Vogel", "2020-2026")
        procedure.add_menu_path("<Image>/Filters/Remove_BG/")

        url_choice = Gimp.Choice.new()
        url_choice.add(
            "cutmatte",
            0,
            "Cutmatte (https://api.cutmatte.com/v1.0/removebg)",
            "Use Cutmatte background removal API",
        )
        url_choice.add(
            "bgclear",
            1,
            "bgclear.ai (https://www.bgclear.ai/api/v1/remove)",
            "Use bgclear.ai background removal API",
        )
        url_choice.add(
            "remove_bg",
            2,
            "remove.bg (https://api.remove.bg/v1.0/removebg)",
            "Use remove.bg API",
        )
        url_choice.add(
            "custom",
            3,
            "Custom URL (enter below)",
            "Use a custom API endpoint URL",
        )

        procedure.add_choice_argument(
            "url_preset",
            "API endpoint",
            "Choose a preset endpoint or select Custom URL",
            url_choice,
            "cutmatte",
            GObject.ParamFlags.READWRITE,
        )
        procedure.add_string_argument(
            "custom_url",
            "Custom URL",
            "Used when 'Custom URL' is selected above",
            "",
            GObject.ParamFlags.READWRITE,
        )
        procedure.add_string_argument(
            "key",
            "API key. You need to create a free API key by visiting the website",
            "API key",
            "Insert HERE",
            GObject.ParamFlags.READWRITE,
        )
        procedure.add_boolean_argument(
            "consent",
            "REQUIRED: I am aware that my image will be sent to the API for processing",
            "consent",
            False,
            GObject.ParamFlags.READWRITE,
        )
        return procedure

    def _build_ssl_contexts(self):
        default_ctx = ssl.create_default_context()
        tls12_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        tls12_ctx.minimum_version = ssl.TLSVersion.TLSv1_2
        tls12_ctx.maximum_version = ssl.TLSVersion.TLSv1_2
        tls12_ctx.load_default_certs()
        return [default_ctx, tls12_ctx]

    def call_api(self, key, url, input_file, output_file):
        headers = {
            "User-Agent": "GIMP-RemoveBG/1.0",
            "Accept": "image/png",
        }
        if key.startswith("bgc_"):
            headers["Authorization"] = f"Bearer {key}"
        else:
            headers["X-Api-Key"] = key

        boundary = "jsdjfhsaasdfadflfhahfhj"
        part_boundary = "--" + boundary

        if not os.path.exists(input_file):
            return False, f"Input file not found: {input_file}"

        with open(input_file, "rb") as f:
            image_content = f.read()

        part_list = [
            part_boundary,
            'Content-Disposition: form-data; name="image_file"; filename="a.png"',
            "Content-Type: image/png",
            "",
            image_content,
            part_boundary,
            'Content-Disposition: form-data; name="size"',
            "",
            "preview",
            "--" + boundary + "--",
            "",
        ]

        body = b"\r\n".join(
            part.encode("utf-8") if isinstance(part, str) else part
            for part in part_list
        )

        last_err = None
        for ctx in self._build_ssl_contexts():
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
            req.add_header("Content-Length", str(len(body)))

            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as response:
                    response_data = response.read()

                with open(output_file, "wb") as out:
                    out.write(response_data)
                return True, None

            except urllib.error.HTTPError as e:
                detail = e.read().decode("utf-8", errors="replace")
                return False, f"HTTP {e.code} ({e.reason}): {detail[:200]}"
            except urllib.error.URLError as e:
                last_err = f"Network/SSL error: {e.reason}"
                if isinstance(e.reason, ssl.SSLEOFError):
                    continue
                return False, last_err
            except Exception as e:
                return False, f"Unexpected error: {e}"

        return False, last_err or "SSL handshake failed"

    @staticmethod
    def try_deleting(file):
        try:
            file.delete()
        except gi.repository.GLib.GError:
            pass

    def _error_return(self, procedure, message):
        domain = GLib.quark_from_string("remove-bg-plugin")
        err = GLib.Error.new_literal(domain, message, 1)
        return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, err)

    # plug-in implementation
    def plug_in_remove_bg(self, procedure, run_mode, image, layers, config, data):
        if run_mode == Gimp.RunMode.INTERACTIVE:
            GimpUi.init("python-fu-remove-bg")
            dialog = GimpUi.ProcedureDialog.new(procedure, config)
            dialog.fill(None)
            if not dialog.run():
                dialog.destroy()
                return procedure.new_return_values(
                    Gimp.PDBStatusType.CANCEL,
                    GLib.Error.new_literal(
                        GLib.quark_from_string("remove-bg-plugin"),
                        "Cancelled",
                        0,
                    ),
                )

        url_preset = config.get_property("url_preset")
        custom_url = (config.get_property("custom_url") or "").strip()
        if url_preset == "custom":
            url = custom_url
        else:
            url = PRESET_URLS.get(url_preset) or custom_url

        if not url:
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            return self._error_return(
                procedure, "Please choose an API endpoint or enter a Custom URL"
            )

        key = config.get_property("key")
        consent = config.get_property("consent")
        if not consent:
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            return self._error_return(
                procedure, "Please agree to the usage of this plugin"
            )

        Gimp.context_push()
        image.undo_group_start()

        height = layers[0].get_height()
        width = layers[0].get_width()

        new_height = float(height)
        new_width = float(width)

        if new_height > 1080.0:
            factor = new_height / 1080.0
            new_height = 1080.0
            new_width = new_width / factor

        if new_width > 1920.0:
            factor = new_width / 1920.0
            new_width = 1920.0
            new_height = new_height / factor

        layer_copy = layers[0].copy()
        image.insert_layer(layer_copy, None, 1)
        layer_copy.scale(int(new_width), int(new_height), 0)

        file1 = Gimp.temp_file("png")
        file2 = Gimp.temp_file("png")

        s = Gimp.file_save(Gimp.RunMode.NONINTERACTIVE, image, file1, None)
        image.remove_layer(layer_copy)

        if not s:
            image.undo_group_end()
            Gimp.context_pop()
            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            self.try_deleting(file1)
            self.try_deleting(file2)
            Gimp.displays_flush()
            return self._error_return(procedure, "Failed to save temporary PNG")

        success, err_msg = self.call_api(key, url, file1.get_path(), file2.get_path())

        if success:
            result_layer = Gimp.file_load_layer(
                Gimp.RunMode.NONINTERACTIVE, image, file2
            )
            image.insert_layer(result_layer, None, 1)
            result_layer.scale(width, height, 0)

            mask = result_layer.create_mask(2)
            layers[0].add_mask(mask)
            image.remove_layer(result_layer)

            image.undo_group_end()
            Gimp.context_pop()

            if run_mode == Gimp.RunMode.INTERACTIVE:
                dialog.destroy()
            self.try_deleting(file1)
            self.try_deleting(file2)
            Gimp.displays_flush()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)

        image.undo_group_end()
        Gimp.context_pop()

        if run_mode == Gimp.RunMode.INTERACTIVE:
            dialog.destroy()
        self.try_deleting(file1)
        self.try_deleting(file2)
        Gimp.displays_flush()
        return self._error_return(procedure, err_msg or "Request failed")


Gimp.main(RemoveBG.__gtype__, sys.argv)
