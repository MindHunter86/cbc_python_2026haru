import pandas as pd
import folium
import openpyxl

df = pd.read_excel("hinan210823.xlsx")

hinan = df[["緯度","経度"]].values

m = folium.Map(location=[35.5339579,139.70083],zoom_start=14)

for data in hinan:
    folium.Marker([data[0],data[1]]).add_to(m)

m.save("hinan.html")