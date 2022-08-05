import gspread
import folium
import pandas as pd
import numpy as np

map = folium.Map(location = [27.70605851,85.30595914], zoom_control = 2)

sa = gspread.service_account(filename = "IncubateNepal.json")
sh = sa.open("Data Base")

wks = sh.worksheet("Sheet1")


lat = []
lon = []


location = wks.get('B2:B27')
    # Create two lists for the loop results to be placed
df = pd.DataFrame(raw_data, columns = ['location'])
df
# For each row in a varible,
for row in df['location']:
    # Try to,
    try:
        # Split the row by comma and append
        # everything before the comma to lat
        lat.append(row.split(',')[0])
        # Split the row by comma and append
        # everything after the comma to lon
        lon.append(row.split(',')[1])
    # But if you get an error
    except:
        # append a missing value to lat
        lat.append(np.NaN)
        # append a missing value to lon
        lon.append(np.NaN)

# Create two new columns from lat and lon
df['latitude'] = lat
df['longitude'] = lon

     



