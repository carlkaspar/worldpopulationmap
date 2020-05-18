import folium
import pandas

data = pandas.read_csv("volcanos.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation = list(data["ELEV"])

def color_producer(elev):
    if  elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

def return_fill(population):
    if population < 2000000:
        return "green"
    elif 1000000 <= population < 10000000:
        return "yellow"
    elif 10000000 <= population < 100000000:
        return "orange"
    else:
        return "red"

map = folium.Map([38.58, -99.09], zoom_start = 6, tiles="OpenStreetMap")


fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, elev in zip(latitude, longitude, elevation):
    fgv.add_child(folium.CircleMarker(location = [lat, lon], radius=7, popup=str(elev) + " m", fill_color=color_producer(elev), color="gray", fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillColor' : return_fill(x['properties']['POP2005'])}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("map.html")