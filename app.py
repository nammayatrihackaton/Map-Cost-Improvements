import streamlit as st
from geopy.geocoders import Nominatim
from shapely.geometry import Point, LineString

st.title("Namma Yatri Map Feature")

geolocator = Nominatim(user_agent="namma-yatri")
location1 = st.text_input("Enter your location:")
location2 = st.text_input("Enter your destination:")

if location1 and location2:
    try:
        # Geocode the user's location and destination
        point1 = Point(geolocator.geocode(location1).point[::-1])
        point2 = Point(geolocator.geocode(location2).point[::-1])
        
        # Calculate the distance between the two points using the Haversine formula
        distance = point1.distance(point2) / 1000  # in km
        st.write(f"Distance: {distance:.2f} km")
        
        # Calculate the fare based on the distance
        fare = distance * 10  # assuming a fare of Rs. 10 per km
        st.write(f"Fare: Rs. {fare:.2f}")
        
        # Draw a line between the two points on a map
        line = LineString([point1, point2])
        st.map(line)
    except:
        st.write("Thanks")
