import folium
import csv
map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)

with open('Database.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        latitude = line[1]
        longitude = line[2]
        description = line[3]


           
        folium.Rectangle([(27.675257767410447, 85.30283779110691),(27.67490210891375, 85.30299177386615)],
        stroke = False,
        fill = True,
        fill_color = "blue",
        fill_opacity = 0.1 ).add_to(map)
map.save("map.html")

''' folium.Polygon([(27.70605851,85.30595914), (27.67490210891375, 85.30299177386615),(28.70605851,85.30595914)], color="blue",
            weight=2,
            fill=True,
            fill_color="orange",
            fill_opacity=0.4).add_to(map)'''
        

