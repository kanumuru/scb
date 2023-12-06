import csv
import json
import sqlite3
import yaml
import xml.etree.ElementTree as ET
import sys
import os
def parse_csv(csv_file_path):
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return list(csv_reader)

def parse_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        return json.load(json_file)

def parse_xml(xml_file_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    return root

def parse_yaml(yaml_file_path):
    with open(yaml_file_path, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)

def create_table(cursor):
    # Replace 'your_table' with the desired table name and adjust column names and types
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sample_table (
            id TEXT PRIMARY KEY,
            name TEXT,
            age TEXT
        )
    ''')

def insert_data_csv(cursor, data):
    # inserting CSV data into the table
    for row in data:
        cursor.execute("INSERT INTO sample_table (id, name, age) VALUES (?, ?, ?);", (row['id'], row['name'], row['age']))
        

def insert_data_json(cursor, data):
    # Inserting JSON data into the table
    for person in data['persons']:
        cursor.execute("INSERT INTO sample_table (id, name, age) VALUES (?, ?, ?)", (person['id'], person['name'], person['age']))

def insert_data_xml(cursor, data):
    # Inserting XML data into the table
    for person_element in data.findall('person'):
        person_data = {
            'id': person_element.find('id').text, 
            'name': person_element.find('name').text,
            'age': person_element.find('age').text
        }
        cursor.execute("INSERT INTO sample_table (id, name, age) VALUES (?, ?, ?)", (person_data['id'], person_data['name'], person_data['age']))

def insert_data_yaml(cursor, data):
    # Inserting YAML data into the table
    for person in data['persons']:
        cursor.execute("INSERT INTO sample_table (id, name, age) VALUES (?, ?, ?)", (person['id'], person['name'], person['age']))
def list_files_in_directory(directory_path):
    try:
        # Get the list of filenames in the specified directory
        filenames = os.listdir(directory_path)

        # Print the filenames
        print("Filenames in '{}' directory:".format(directory_path))
        for filename in filenames:
            print(filename)

    except FileNotFoundError:
        print("Directory not found: '{}'".format(directory_path))
    except PermissionError:
        print("Permission error: Unable to access '{}' directory.".format(directory_path))
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    # Replace 'your_database.db' with the desired SQLite database name
    database_name = 'scb.db'
    # Connect to SQLite database
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    # Create the table if it doesn't exist
    create_table(cursor)

    filepath = "/Users/kanumururajesh/Desktop/tmp/scb/automation/task4/dataset/"

    filenames = os.listdir(filepath)
    print(filenames)
    for filename in filenames:
        print(filename)
        name, extension = filename.split('.')
        print(name, extension)

        if extension == 'csv':
            csv_data = parse_csv(filepath+filename)
            insert_data_csv(cursor, csv_data)
            
        elif extension == 'json':
            json_data = parse_json(filename)
            insert_data_json(cursor, json_data)

        elif extension == 'xml':
            xml_data = parse_xml(filename)
            insert_data_xml(cursor, xml_data)

        elif extension == 'yaml' or extension == 'yml':
            yaml_data = parse_yaml(filename)
            insert_data_yaml(cursor, yaml_data)

        else:
            print("Invalid file format")
        os.remove(filepath+filename)
    # Commit changes and close the database connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
