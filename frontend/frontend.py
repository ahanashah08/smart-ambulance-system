import streamlit as st
import requests
from streamlit_folium import folium_static
import folium

st.title("🚑 Smart Ambulance System")
location = st.text_input("Enter Your Location:")

if st.button("Find Nearest Hospital"):
    response = requests.get(f"http://127.0.0.1:5000/find_hospital?location={location}")
    data = response.json()

    if "error" in data:
        st.error("No hospital found")
    else:
        ambulance_map = folium.Map(location=[data['lat'], data['lon']], zoom_start=12)
        folium.Marker(
            location=[data['lat'], data['lon']],
            popup=data['name'],
            icon=folium.Icon(color="red", icon="plus"),
        ).add_to(ambulance_map)

        folium_static(ambulance_map)