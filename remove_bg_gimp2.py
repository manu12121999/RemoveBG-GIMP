#!/usr/bin/env python
import tempfile
from sys import platform
import urllib2
import ssl

from gimpfu import *


def remove_background(image, layer, key):
    pdb.gimp_image_undo_group_start(image)

    # input
    height = pdb.gimp_drawable_height(layer)
    width = pdb.gimp_drawable_width(layer)

    new_height = float(height)
    new_width = float(width)

    if new_height > 1080.0:  # scale down
        factor = new_height / 1080.0
        new_height = 1080
        new_width = int(new_width / factor)

    if new_width > 1920.0:
        factor = new_width / 1920.0
        new_width = 1920
        new_height = int(new_height / factor)

    layer_copy = pdb.gimp_layer_copy(layer, 1)
    pdb.gimp_image_insert_layer(image, layer_copy, None, 0)
    pdb.gimp_layer_scale(
        layer_copy, new_width, new_height, 0
    )  # make a copy and scale it down

    temp = tempfile.gettempdir()
    if platform == "linux" or platform == "linux2":
        f = "/tmp/temp.png"
        f2 = "/tmp/temp2.png"
    else:
        f = temp + "\\temp.png"
        f2 = temp + "\\temp2.png"

    pdb.file_png_save_defaults(image, layer_copy, f, f)

    pdb.gimp_image_remove_layer(image, layer_copy)

    # remove.bg
    url = "https://api.remove.bg/v1.0/removebg"
    headers = {"X-Api-Key": key}

    boundary = "jsdjfhsaasdfadflfhahfhj"
    part_boundary = '--' + boundary

    # Add the files to upload
    image_content = open(f,"rb").read()

    part_list = []
    part_list.append(part_boundary)
    part_list.append('Content-Disposition: form-data; name="image_file"; filename="a.png"')
    part_list.append('Content-Type: image/png')
    part_list.append('')
    part_list.append(image_content)
    part_list.append('--' + boundary + '--')
    part_list.append('')
    
    body = '\r\n'.join(part_list)

    req = urllib2.Request(url, body, headers)
    req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    req.add_header('Content-length', len(body))

    context = ssl._create_unverified_context()
    response = urllib2.urlopen(req, context = context).read()
    with open(f2, "wb") as out:
        out.write(response)

    # output
    outlayer = pdb.gimp_file_load_layer(image, f2)
    # because you cant scale without adding the layer
    pdb.gimp_image_insert_layer(image, outlayer, None, 0)

    pdb.gimp_layer_scale(outlayer, width, height, 0)
    # pdb.gimp_layer_resize(outlayer, width, height, 0, 0)

    mask = pdb.gimp_layer_create_mask(outlayer, 2)
    pdb.gimp_layer_add_mask(layer, mask)
    pdb.gimp_image_remove_layer(image, outlayer)

    pdb.gimp_image_undo_group_end(image)


register(
    "python-fu-remove_background",
    "Easy Way to remove the BG of a Picture",
    "Description.",
    "Manuel V.",
    "M",
    "2020",
    "remove_background",
    "*",
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "input layer", None),
        (PF_STRING, "key", "Remove_bg KEY", "INSERT_YOUR_KEY_HERE"),
    ],
    [],
    remove_background,
    menu="<Image>/Filters",
)

main()
