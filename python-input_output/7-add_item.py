#!/usr/bin/python3
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if not os.path.exists(filename):
    data = []
else:
    data = load_from_json_file(filename)

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
