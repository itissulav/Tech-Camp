import gspread
import folium

map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)

sa = gspread.service_account(filename = "techcamp-358501-250f1bf4f51b.json")
sh = sa.open("TechCamp Data Base")

wks = sh.worksheet("Sheet1")

map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)


latitude1 = float(wks.acell('B2').value) 
longitude1 = float(wks.acell('C2').value)

folium.Marker(location = [latitude1, longitude1], popup = "hello").add_to(map)

map.save("map.html")



