#!/usr/bin/env python3


import json
import csv


def convert_csv_to_json(csv_filename):
    try:
        data = []
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except Exception as e:
        print(f"An error ocurred: {e}")
        return False
