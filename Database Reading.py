import folium
import csv

with open('Database.csv') as file:
    reader = csv.reader(file)
    next (reader)
    for line in reader:
      print(line(2))