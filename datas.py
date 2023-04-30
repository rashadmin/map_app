import pandas as pd
from codes import return_geomtry_df
import streamlit as st


@st.cache(allow_output_mutation=True)
def call_data(num):
    df = pd.read_csv('datasets/nigeria_state_boundaries.csv')#false
    df_1 = pd.read_csv('datasets/all_transmission_substations.csv')#false
    df_2 = pd.read_csv('datasets/transmission_lines.csv')#True
    df_3 = pd.read_csv('datasets/power_plants.csv')#False
    #df_4 = pd.read_csv('datasets/cluster_offgrid.csv')#False
    #df_5 = pd.read_csv('datasets/disco_coverage.csv')#True
    #df_6 = pd.read_csv('datasets/distribution_line_se4all24.csv')#False
    df_7 = pd.read_csv('datasets/minigrids.csv')
    #df_8 = pd.read_csv('datasets/distribution_line_kaduna_electric.csv')
    #df_9 = pd.read_csv('datasets/distribution_line_kedco.csv')
    #df_10 = pd.read_csv('datasets/modelled_grid_original.csv')
    #df_11 = pd.read_csv('datasets/cluster_all.csv')
    #df_12 = pd.read_csv('datasets/electrical_grid_nigeria_15.csv')
    
    
        
    df = return_geomtry_df(df,'geom',diff_espg=True)
    df_1 = return_geomtry_df(df_1,'geom',diff_espg=True)
    df_2 = return_geomtry_df(df_2,'geometry')
    df_3 = return_geomtry_df(df_3,'geom',diff_espg=True)
    #df_4 = return_geomtry_df(df_4,'geom')
    #df_5 = return_geomtry_df(df_5,'geom',diff_espg=True)
    #df_6 = return_geomtry_df(df_6,'the_geom')
    df_7 = return_geomtry_df(df_7,'geom',diff_espg=True)
    
    if num ==1:
        return df,df_1,df_2,df_3,df_7#,df_5,df_6,df_7