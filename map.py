from streamlit_folium import st_folium
import numpy as np
from folium.features import GeoJson
import streamlit as st
st.set_page_config(layout="wide")
import folium
from datas import call_data
import pandas as pd
import time
import geopandas as gpd
#read df


# read wrangled_df
nigeria_state = gpd.read_file('wrangled_datasets/nigeria_state_boundaries_dir/nigeria_state_boundaries.shp',)

st.title('INTERACTIVE DASH BOARD')

nigeria_map = folium.Map(location=[9.081999, 8.675277], zoom_start=6)



lga_df = gpd.read_file('lga/nga_admbnda_adm2_osgof_20170222.shp',)
substations = gpd.read_file('wrangled_datasets/substation_dir/all_transmission_substations.shp')
power_plants = gpd.read_file('wrangled_datasets/power_plant_dir/power_plants.shp')
mini_grid = gpd.read_file('wrangled_datasets/mini_grid_dir/minigrids.shp')
state_selected = st.selectbox('State', options = np.insert(nigeria_state['adm1_en'].unique(),0,'All_States'))
st.write(state_selected)



if state_selected == 'All_States':
    nigeria_map = folium.Map(location=[9.081999, 8.675277])
    nigeria_states = nigeria_state['geometry']
    folium.GeoJson(nigeria_states,  
                   style_function=lambda feature: {'color': 'green'}
                    ).add_to(nigeria_map)
    sub_station = substations['admin1Name'].shape[0]
    power_plant = power_plants['admin1Name'].shape[0]
    minigrid = mini_grid['admin1Name'].shape[0]
    cols = st.columns(3)
    with cols[0]:
        st.write(f'SUBSTATIONS:{sub_station} ')
    with cols[1]:
        st.write(f'POWERPLANTS: {power_plant} ')
    with cols[2]:
        st.write(f'MINIGRIDS: {minigrid}')
    col = st.columns([1,8,1])
    with col[1]:
        st_data = st_folium(nigeria_map,width=1200,height=600,zoom=6)
        
else:
    index = nigeria_state[nigeria_state['adm1_en'] == state_selected].index.values[0]
    nigeria_map = folium.Map(location=[nigeria_state.loc[index,'lat'], nigeria_state.loc[index,'lon']], zoom_start=8    )
    #geojson = GeoJson(data=nigeria_state.loc[index,'geometry'])
    folium.GeoJson(nigeria_state['geometry'][index:index+1]).add_to(nigeria_map)
    lga_geom = lga_df[lga_df['admin1Name']==state_selected]
    sub_station = substations[substations['admin1Name']==state_selected].shape[0]
    power_plant = power_plants[power_plants['admin1Name']==state_selected].shape[0]
    minigrid = mini_grid[mini_grid['admin1Name']==state_selected].shape[0]
    folium.GeoJson(lga_geom['geometry'],style_function=lambda feature: {'color': 'green'}).add_to(nigeria_map)
    st.write(index)
    #st.write((nigeria_state['geometry'][0:1]))
    cols = st.columns(3)
    with cols[0]:
        st.write(f'SUBSTATIONS:{sub_station}')
    with cols[1]:
        st.write(f'POWERPLANTS: {power_plant} ')
    with cols[2]:
        st.write(f'MINIGRIDS: {minigrid}')
    col = st.columns([1,8,1])
    with col[1]:
        st_data = st_folium(nigeria_map,width=1200,height=600,zoom=8)
    

'''options = ['Power_Station','SubStations','Transmission Lines','Distribution Lines']
check = st.selectbox('What to Check', options=options)

if check == 'Power_Station':
    df_present = df_3['geometry']
    folium.GeoJson(df_present,
                   style_function=lambda feature: {'color': 'red'}
                    ).add_to(nigeria_map)
elif check == 'SubStations':
    df_present = df_1['geometry']
    folium.GeoJson(df_present,
                   style_function=lambda feature: {'color': 'red'}
                    ).add_to(nigeria_map)
elif check== 'Transmission Lines':
    for index, row in df_2.to_crs('4326').iterrows():
        folium.PolyLine(locations=row['geometry'].coords).add_to(nigeria_map)
elif check == 'Distribution Lines':
    for index, row in df_7.to_crs('4326').iterrows():
        folium.PolyLine(locations=row['geometry'].coords).add_to(nigeria_map)
        
with st.spinner('Wait for it...'):'''
    #time.sleep(5)






