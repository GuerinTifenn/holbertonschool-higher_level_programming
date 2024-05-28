#!/usr/bin/python3
"""function that takes the CSV filename and writes the JSON data"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON format.
    Args: csv_filename (str): The filename of the CSV file.
    Returns: bool: True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        json_data = json.dumps(data, indent=4)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print("Error: File '{}' not found.".format(csv_filename))
        return False
