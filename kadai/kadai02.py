import pandas as pd
import folium

df = pd.read_csv('141305_care_service.csv', encoding='cp932')

print(f'found {len(df)} records')
print(df.columns.values)
print('building HTML map ...')

store = df[['緯度','経度','介護サービス事業所名称','ID','電話番号','郵便番号','URL']].values

m = folium.Map(location=[35.535947300324544, 139.7028184738351],zoom_start=32)

for data in store:
    # wtf ...
    url = '#' if not isinstance(data[6], str) else data[6]
    urlhtml = '<a href="{url}">https://citi.kawasaki.jp/</a>' if url != '#' else 'no data'

    tpl = f'ID: {data[1]}<br />Name: {data[2]}<br /><br />Phone: {data[4]}<br />ZIP: {data[5]}<br />Link: {urlhtml}'
    folium.Marker(
        location=[data[0],data[1]],
        tooltip=data[2],
        popup=folium.Popup(tpl, max_width=250),
        icon=folium.Icon(color="lightgreen", icon="pushpin")
    ).add_to(m)

m.save('care.html')