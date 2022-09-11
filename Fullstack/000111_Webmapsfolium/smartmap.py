import folium
import pandas as pd


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

#latitude longitude  # tiles ="Stamen Terrain"
map = folium.Map(location =[48, -120]  , zoom_start = 8 , tiles ="Stamen Terrain")
#organized feature group
fg = folium.FeatureGroup(name ="map")

#add points
for lt, ln, el, name in zip(latitudelst, longitudelst, elevationlst, namelst):
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(str(el)+"m")
    ,radius =6 ,fillcolor= color_producer(el) ,color ="grey" ,fill_opacity= 0.7     )   )

#add geojson data
fg.add_child(folium.GeoJson( data = open('world.json','r' ,encoding= 'utf-8-sig').read(),
style_function = lambda x : {'fillcolor':'green' if x['properties'] ['POP2005'] < 10000000 
else 'orange' if  10000000  <= x['properties']['POP2005'] <=  20000000
else 'red' }))  

map.add_child(fg)
#create the html
map.save("smartmap.html")

print(df)
print('-----latitudes------')
print(latitudedf)














