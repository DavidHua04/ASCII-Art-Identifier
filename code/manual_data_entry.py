import csv
import json
import hashlib
import tkinter as tk
from tkinter import simpledialog, messagebox

def make_id(ascii_art, type_field, length=8):
    # Deterministic: hash of ascii_art + type_field, avoids collisions and easy to trace
    h = hashlib.sha256((ascii_art + type_field).encode('utf-8')).hexdigest()
    return f"{type_field}_{h[:length]}"

def json_escape(text):
    return json.dumps(text)[1:-1]  # Strip quotes

def append_to_csv(row, csv_file='../data/ASCII_dict.csv'):
    # Append a row, add header if file does not exist
    import os
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'ASCII_art', 'type', 'expected_feature'], quoting=csv.QUOTE_ALL)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def input_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Multiline ASCII input
    ascii_art = simpledialog.askstring("ASCII Art Entry", "Paste your ASCII art (multiline supported):")
    if not ascii_art:
        messagebox.showerror("Error", "No ASCII art entered.")
        return

    # Type selection
    type_choices = ["kaomoji", "multiline_ascii", "noise"]
    type_field = simpledialog.askstring("Type Entry", f"Enter type ({'/'.join(type_choices)}):")
    if not type_field or type_field not in type_choices:
        messagebox.showerror("Error", f"Type must be one of: {', '.join(type_choices)}.")
        return

    # Feature input
    features = simpledialog.askstring("Features", "Enter expected features (separated by '|'):")
    if not features:
        messagebox.showerror("Error", "No features entered.")
        return

    # Build row
    row = {
        "id": make_id(ascii_art, type_field),
        "ASCII_art": json_escape(ascii_art),
        "type": type_field,
        "expected_feature": features
    }
    append_to_csv(row)
    messagebox.showinfo("Done", f"Entry added to ASCII_dict.csv:\n\n{row}")

if __name__ == "__main__":
    input_gui()
