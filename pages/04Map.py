import streamlit as st
import folium
from streamlit_folium import st_folium

st.title('Live Ride Tracking')

center = [24.8607, 67.0011]  # Karachi coordinates
map_folium = folium.Map(location=center, zoom_start=12)

# Add markers
folium.Marker(
    location=center, 
    popup='SHE Hub', 
    icon=folium.Icon(color='pink')
).add_to(map_folium)

st_folium(map_folium, width=700, height=500)
if st.session_state["page"] == "Map":
    map()  # define this function to show your map content
