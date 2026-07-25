import pandas as pd
import folium

df = pd.read_csv('kyusui.csv', encoding='CP932')
store = df[['緯度','経度','拠点名']].values
m = folium.Map(location=[35.532957,139.198863],zoom_start=16)

for data in store:
    folium.Marker([data[0],data[1]],tooltip=data[2]).add_to(m)

m.save('kyusui.html')

print(len(df))
print(df.columns.values)