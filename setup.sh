#!/bin/sh
#Run this file in your plugins directory, if the plug in does not show up in GIMP
chmod +x remove_background.py
python -m pip install --user virtualenv
python -m virtualenv gimpenv
source gimpenv/bin/activate
python -m install requests
deactivate
