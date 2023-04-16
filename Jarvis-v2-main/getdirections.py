import folium
import requests

def get_directions(origin, destination):
    url = "https://routing.openstreetmap.de/routed-car/route/v1/driving/"
    params = dict(
        waypoints=';',  # You can add intermediate waypoints separated by ';'
        alternatives='false',
        steps='true',
        annotations='true',
        geometries='geojson',
        overview='full'
    )
    params['sources'] = '0'
    params['destinations'] = '1'
    params['coordinates'] = f"{origin[1]},{origin[0]};{destination[1]},{destination[0]}"
    resp = requests.get(url=url, params=params)
    data = resp.json()
    route = data['route'][0]
    distance = route['distance'] / 1000  # in km
    duration = route['duration'] / 3600  # in hours
    steps = route['legs'][0]['steps']
    
    # Print the distance, duration and steps
    print(f"Distance: {distance:.2f} km")
    print(f"Duration: {duration:.2f} hours")
    print("Steps:")
    for i, step in enumerate(steps):
        print(f"{i+1}. {step['name']} ({step['distance']/1000:.2f} km, {step['duration']/60:.2f} min)")
    
    # Show the route on a map
    m = folium.Map(location=origin, zoom_start=13)
    folium.PolyLine(locations=[list(reversed(coord)) for coord in route['geometry']['coordinates']]).add_to(m)
    folium.Marker(location=origin, tooltip="Origin").add_to(m)
    folium.Marker(location=destination, tooltip="Destination").add_to(m)
    m.save('route.html')


get_directions(origin = "19.09332549331524, 73.00913691284904" , destination="19.074644308806263, 72.99780417633607")