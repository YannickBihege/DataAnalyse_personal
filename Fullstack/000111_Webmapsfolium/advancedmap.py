import folium
import pandas as pd



html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""



#latitude longitude
map = folium.Map(location =[48, -120]  , zoom_start = 8 , tiles ="Stamen Terrain")
print(type(map))


#organized feature group
fg = folium.FeatureGroup(name ="map")



#read from text
df = pd.read_csv('volcanoes.txt')
latitudedf = df["LAT"]
longitudedf = df["LON"]
elevationdf = df['ELEV']


latitudelst = list(latitudedf)
longitudelst = list(longitudedf)
elevationlst = list(elevationdf)
namelst = list(df["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else:
        return "red"



#add points
for lt, ln, el, name in zip(latitudelst, longitudelst, elevationlst, namelst):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    # fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el) ))  )
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el)) ,radius =6 ,fillcolor= color_producer(el) ,color ="grey" ,fill_opacity= 0.7     )   )


map.add_child(fg)
#create the html
map.save("advancedmap.html")

print(df)
print('-----latitudes')
print(latitudedf)














