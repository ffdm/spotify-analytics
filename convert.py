"""
JSON -> CSV converter based on
https://www.geeksforgeeks.org/convert-json-to-csv-in-python/
"""
import csv
import json

# Open JSON file 
with open('data.json') as jsonFile:
    data = json.load(jsonFile)
    # Name columns
    column_names = ["name", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness",
        "liveness", "valence", "tempo", "type", "id", "uri", "track_href", "analysis_url", "duration_ms", "time_signature"]
    data_list = []
    for key in data:
        row = [key]
        row.extend(data[key].values())
        data_list.append(row)
    
    # Write csv file
    filename = "data.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(column_names)
        csvwriter.writerows(data_list)