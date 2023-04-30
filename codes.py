import geopandas as gpd
import pyproj
from shapely.geometry import Point
from shapely import wkt
import numpy as np
import pandas as pd
from shapely.geometry import Point, MultiPolygon

#gs = gpd.GeoSeries.from_wkt(df['geom'])
#z = gpd.GeoDataFrame(df,geometry=gs,crs='3857')

# Define the source and target coordinate systems
#src_crs = pyproj.CRS.from_epsg(3857)  # UTM Zone 10N
#target_crs = pyproj.CRS.from_epsg(4326)  # WGS84

# Create a transformer object to convert between the coordinate systems
#transformer = pyproj.Transformer.from_crs(src_crs, target_crs, always_xy=True)
#point = z['geometry']
#df['long'],df['lats'] = transformer.transform(point.x, point.y)




def return_geomtry_df(df,column_name,diff_espg=False):
    df = df.dropna(subset=column_name)
    types = str(df[column_name][2]).split(' ')[0][-6:]
    
    espg = {True:'3857',False:4326}
    # Define the state boundary as a MultiPolygon object
    lga_df = gpd.read_file('datasets/lga/nga_admbnda_adm2_osgof_20170222.shp',)
    state_df = pd.read_csv('datasets/nigeria_state_boundaries.csv')
    state_geo = gpd.GeoSeries.from_wkt(state_df['geom'])
    state_column_df = gpd.GeoDataFrame(state_df,geometry=state_geo,crs=3857).to_crs('4326')
    
    if types != 'STRING':
        column_geo = gpd.GeoSeries.from_wkt(df[column_name])
        column_df = gpd.GeoDataFrame(df,geometry=column_geo,crs=espg[diff_espg]).to_crs('4326')

        column_locator = {'Lga':[get_index(lga_df,lga) for lga in lga_df['geometry'] for location in column_df['geometry'] if lga.contains(location)],
                         'geometry': [location for lga in lga_df['geometry'] for location in column_df['geometry'] if lga.contains(location)] }
    else:
        column_geo = gpd.GeoSeries.from_wkt(df[column_name].drop_duplicates())
        column_df = gpd.GeoDataFrame(df,geometry=column_geo,crs=espg[diff_espg]).to_crs('4326')
        column_locator = {'Lga':[get_index(lga_df,lga) for lga in lga_df['geometry'] for location in column_df['geometry'] if lga.intersects(location)],
                         'geometry': [location for lga in lga_df['geometry'] for location in column_df['geometry'] if lga.intersects(location)] }
    st_df = pd.DataFrame().from_dict(column_locator).drop_duplicates(subset='geometry')
    st_df = gpd.GeoDataFrame(st_df,geometry='geometry',crs='3857')
    complete_df = pd.merge(column_df,st_df)
    state_lga = lga_df[['admin2RefN','admin1Name']]
    complete_df = pd.merge(complete_df,state_lga,left_on='Lga',right_on='admin2RefN',).drop('admin2RefN',axis=1)
    return complete_df
def get_index(lga_df,lga):
    index = lga_df.index[lga_df['geometry'] == lga].to_list()[0]
    lga_name = lga_df.loc[index,'admin2Name']
    return lga_name

def return_state_geometry(df,column):
    lga_df = gpd.read_file('lga/nga_admbnda_adm2_osgof_20170222.shp',)
    column_geo = gpd.GeoSeries.from_wkt(df[column_name])
    column_df = gpd.GeoDataFrame(df,geometry=column_geo,crs='3857').to_crs('4326')
    column_locator = {'Lga':[get_index(lga_df,lga) for lga in lga_df['geometry'] for location in column_df['geometry'] if location.contains(lga)],
                         'geometry': [location for lga in lga_df['geometry'] for location in column_df['geometry'] if location.contains(lga)] }
    st_df = pd.DataFrame().from_dict(column_locator).drop_duplicates(subset='geometry')
    st_df = gpd.GeoDataFrame(st_df,geometry='geometry',crs='3857')
    complete_df = pd.merge(column_df,st_df)
    return complete_df