import folium

import pandas as pd
print(dir(folium))
#print(help(folium.Map))

#latitude longitude
# map = folium.Map(location =[50.1, 8.641,]  , zoom_start = 8)

map = folium.Map(location =[50.1, 8.641,]  , zoom_start = 8 , tiles ="Stamen Terrain")
# #Add elements
# map.add_child(folium.Marker(location =[50.1, 8.641,]  , popup="Marker IBC"  , icon = folium.Icon(color ="green")))

print(type(map))

#organized feature group
fg = folium.FeatureGroup(name ="map")


#fg.add_child(folium.Marker(location =[50.1, 8.641,]  , popup="Marker IBC"  , icon = folium.Icon(color ="green")))

#mark multiple points
# for coordinates in [[50.1, 8.641, 222],[ 8.641, 50.1, 2222] ,[25.05, 4.2305 ,2222]]:
#     fg.add_child(folium.Marker(location = coordinates , popup="Marker IBC"  , icon = folium.Icon(color ="green")))

# map.add_child(fg)



#read from text
df = pd.read_csv('volcanoes.txt')
latitudedf = df["LAT"]
longitudedf = df["LON"]
elevationdf = df['ELEV']


latitudelst = list(latitudedf)
longitudelst = list(longitudedf)
elevationlst = list(elevationdf)


for lt , ln , el in zip(latitudelst, longitudelst , elevationlst):
    print(type(el))
    fg.add_child(folium.Marker(location = [lt,ln , el] , popup= folium.Popup(str(el)+"m")  , icon = folium.Icon(color ="green")))

#create the html
map.save("map.html")

print(df)
print('-----latitudes')
print(latitudedf)














