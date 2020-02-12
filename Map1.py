import folium
import pandas

data = pandas.read_csv("Volcanoes.csv")
MarkerListLon = list(data["LON"])
MarkerListLat = list(data["LAT"])
MarkerListName = list(data["NAME"])
MarkerListElev = list(data["ELEV"])

def marker_colours(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [19.197773, 72.994639], zoom_start = 16)

fgm = folium.FeatureGroup(name = "Markers")
for lt, ln, name, elev in zip(MarkerListLat, MarkerListLon, MarkerListName, MarkerListElev):
    fgm.add_child(folium.CircleMarker(location = [lt, ln], popup = str(name) + ", " + str(elev) + " m", radius = 6, fill_color = marker_colours(elev), color = marker_colours(elev), fill = True, fill_opacity = 0.7))

map.add_child(fgm)

map.save("DemoMap.html")
