import json
import csv
import hashlib

def make_id(text, type_prefix="kao", length=8):
    # Use a hash of ascii_art and prefix for type
    h = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return f"{type_prefix}_{h[:length]}"

def json_escape(text):
    # Ensures multiline and unicode preserved as \uXXXX and \n
    return json.dumps(text)[1:-1]  # removes surrounding quotes


with open('../data/emoticon_dict.json', encoding='utf-8') as f:
    data = json.load(f)

with open('../data/emoticon_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'ASCII_art', 'type', 'expected_feature']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for ascii_art, content in data.items():
        type_field = 'kaomoji'  # can extend later
        row = {
            'id': make_id(ascii_art, type_field),
            'ASCII_art': json_escape(ascii_art),  # store as json-escaped string
            'type': type_field,
            'expected_feature': '|'.join(content['new_tags'])
        }
        writer.writerow(row)