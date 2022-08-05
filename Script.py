import gspread
import folium

map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)

sa = gspread.service_account(filename = "techcamp-358501-250f1bf4f51b.json")
sh = sa.open("TechCamp Data Base")

wks = sh.worksheet("Sheet1")

map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)


for i in range(2,8):

    nameofplace = wks.cell(i,1).value
    latitude1 = float(wks.cell(i,2).value)
    longitude1 = float(wks.cell(i,3).value)

    typeofsite = wks.cell(i,10).value

    if typeofsite == "road":
        nameofplace = wks.cell(i,1).value
        latitude1 = float(wks.cell(i,2).value)
        longitude1 = float(wks.cell(i,3).value)
        latitude2 = float(wks.cell(i,4).value)
        longitude2 = float(wks.cell(i,5).value)
        folium.PolyLine([(latitude1,longitude1), (latitude2,longitude2)], 
        fill = True,
        fill_color = "red" ).add_to(map)


    elif typeofsite == "site":
        nameofplace = wks.cell(i,1).value
        latitude1 = float(wks.cell(i,2).value)
        longitude1 = float(wks.cell(i,3).value)
        latitude2 = float(wks.cell(i,4).value)
        longitude2 = float(wks.cell(i,5).value)
        latitude3 = float(wks.cell(i,6).value)
        longitude3 = float(wks.cell(i,7).value)
        latitude4 = float(wks.cell(i,8).value)
        longitude4 = float(wks.cell(i,9).value)
        folium.Polygon([(latitude1,longitude1), (latitude2,longitude2), (latitude3,longitude3), (latitude4, longitude4)],
        fill_color = "red").add_to(map)
    
    folium.Polygon([(27.633416, 85.363211),(27.630892, 85.357601), (27.623009, 85.357996), (27.625261, 85.365490)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.747524, 85.301330),(27.745691, 85.303833), (27.748593, 85.305386), (27.750235, 85.302538)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.716341, 85.341454),(27.711854, 85.348055), (27.730324, 85.353006), (27.732410, 85.338625)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.707310, 85.376308),(27.704701, 85.383734), (27.716285, 85.389393), (27.711067, 85.374069)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.681298, 85.358686),(27.676010, 85.358589), (27.675584, 85.369569), (27.680957, 85.370051)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.787760, 85.336185),(27.781824, 85.334351), (27.781445, 85.341904), (27.786041, 85.344251)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.664474, 85.274151),(27.662638, 85.279892), (27.666776, 85.280320), (27.667006, 85.276332)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.617388, 85.428850),(27.610376, 85.437528), (27.628094, 85.451193), (27.629169, 85.435916)], fill_color = "orange").add_to(map)
    folium.Polygon([(27.725705, 85.435187),(27.720802, 85.434755), (27.721630, 85.440798), (27.724814, 85.443459)], fill_color = "orange").add_to(map)
    folium.CircleMarker( location = [27.725729864652937, 85.43233724449269], radius=15).add_to(map)

    def poptext():
        return "<img src = '1.jpg' > \nStarted On: 2079/04/20 \n Ending Date: 2079/04/26 \n<p> Description : Fixing Drainage \t\nInquery: info@smth.com \n\n<button> Report </button>"

    folium.Marker(
        location = [latitude1, longitude1], 
        popup = poptext(), 
        icon=folium.Icon(color="red", icon="info-sign"),
        ).add_to(map)


map.save("map.html")



