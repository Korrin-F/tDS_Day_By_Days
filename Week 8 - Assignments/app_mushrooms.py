#---------------------------------
# IMPORTING
#---------------------------------

import pandas as pd
import numpy as np
# streamlit
import streamlit as st
import streamlit_echarts as st_echarts
# visualising data
import matplotlib.pyplot as plt
import seaborn as sns
# splitting data
from sklearn.model_selection import train_test_split
# models
from sklearn import tree
# metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

# DATASET
df = pd.read_csv('mushrooms_dummies.csv')

#---------------------------------
# APP DETAILS
#---------------------------------

# MAIN PAGE
st.title('Mushroom Classification App')

# SIDEBAR
st.sidebar.image('mushrooms.jpg', width=300)
st.sidebar.header('Parameters:')

#---------------------------------
# USER INPUT
#---------------------------------
def user_input():
    def assign_dict(parameter, dictionary):
        for i in dictionary:
            if i == parameter:
                dictionary[i] = 1
            else:
                dictionary[i] = 0

    # CAP SHAPE  
    # bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
    # Radio Button - Cap Shape
    cap_shape = st.sidebar.radio('What is the cap shape?', ['Bell', 'Conical', 'Flat', 'Knobbed', 'Sunken', 'Convex'])
    # Dictionary - Cap Shape
    cap_shape_dict = {'Bell': 0, 'Conical': 0, 'Flat': 0, 'Knobbed': 0, 'Sunken': 0, 'Convex': 0}
    assign_dict(cap_shape, cap_shape_dict)


           
    # CAP SURFACE 
    # fibrous=f, grooves=g, scaly=y, smooth=s
    cap_surface = st.sidebar.radio('What is the cap surface?', ['Fibrous', 'Grooves', 'Smooth', 'Scaly',])
    cap_surface_dict = {'Fibrous': 0, 'Grooves': 0, 'Smooth': 0, 'Scaly': 0}

    for i in cap_surface_dict:
        if i == cap_surface:
            cap_surface_dict[i] = 1
        else:
            cap_surface_dict[i] = 0


   

    # CAP COLOR brown=n,buff=b,cinnamon=c,gray=g,green=r,pink=p,purple=u,red=e,white=w,yellow=y
    cap_color = st.sidebar.radio('What is the cap color?', ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow',])
    cap_color_n = 0
    cap_color_b = 0
    cap_color_c = 0
    cap_color_g = 0
    cap_color_r = 0
    cap_color_p = 0
    cap_color_u = 0
    cap_color_e = 0
    cap_color_w = 0
    cap_color_y = 0
    match cap_color:
        case 'Brown':
            cap_color_n = 1
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Buff':
            cap_color_n = 0
            cap_color_b = 1
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Cinnamon':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 1
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Gray':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 1
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Green':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 1
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Pink':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 1
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Purple':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 1
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 0
        case 'Red':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 1
            cap_color_w = 0
            cap_color_y = 0
        case 'White':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 1
            cap_color_y = 0
        case 'Yellow':
            cap_color_n = 0
            cap_color_b = 0
            cap_color_c = 0
            cap_color_g = 0
            cap_color_r = 0
            cap_color_p = 0
            cap_color_u = 0
            cap_color_e = 0
            cap_color_w = 0
            cap_color_y = 1

    # BRUISES
    bruises = st.sidebar.radio('Are there bruises?', ['Bruises', 'No Bruises'])
    # ODOR
    odor = st.sidebar.radio('What is the odor?', ['Almond', 'Anise', 'Creosote', 'Fishy', 'Foul', 'Musty', 'None', 'Pungent', 'Spicy'])
    # GILL ATTACHMENT
    gill_attachment = st.sidebar.radio('What is the gill attachment?', ['Attached', 'Descending', 'Free', 'Notched'])
    # GILL SPACING
    gill_spacing = st.sidebar.radio('What is the gill spacing?', ['Close', 'Crowded', 'Distant'])
    # GILL SIZE
    gill_size = st.sidebar.radio('What is the gill size?', ['Broad', 'Narrow'])
    # GILL COLOR
    gill_color = st.sidebar.radio('What is the gill color?', ['Black', 'Brown', 'Buff', 'Chocolate', 'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow'])
    # STALK SHAPE
    stalk_shape = st.sidebar.radio('What is the stalk shape?', ['Enlarging', 'Tapering'])
    # STALK ROOT
    stalk_root = st.sidebar.radio('What is the stalk root?', ['Bulbous', 'Club', 'Equal', 'Rhizomorphs', 'Rooted', 'Missing'])
    # STALK SURFACE ABOVE RING
    stalk_surface_above_ring = st.sidebar.radio('What is the stalk surface above ring?', ['Fibrous', 'Scaly', 'Silky', 'Smooth'])
    # STALK SURFACE BELOW RING
    stalk_surface_below_ring = st.sidebar.radio('What is the stalk surface below ring?', ['Fibrous', 'Scaly', 'Silky', 'Smooth'])
    # STALK COLOR ABOVE RING
    stalk_color_above_ring = st.sidebar.radio('What is the stalk color above ring?', ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'])
    # STALK COLOR BELOW RING
    stalk_color_below_ring = st.sidebar.radio('What is the stalk color below ring?', ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'])
    # VEIL TYPE
    veil_type = st.sidebar.radio('What is the veil type?', ['Partial', 'Universal'])
    # VEIL COLOR
    veil_color = st.sidebar.radio('What is the veil color?', ['Brown', 'Orange', 'White', 'Yellow'])
    # RING NUMBER
    ring_number = st.sidebar.radio('What is the ring number?', ['None', 'One', 'Two'])
    # RING TYPE
    ring_type = st.sidebar.radio('What is the ring type?', ['Cobwebby', 'Evanescent', 'Flaring', 'Large', 'None', 'Pendant', 'Sheathing', 'Zone'])
    # SPORE PRINT COLOR
    spore_print_color = st.sidebar.radio('What is the spore print color?', ['Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow'])
    # POPULATION
    population = st.sidebar.radio('What is the population?', ['Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary'])
    # HABITAT
    habitat = st.sidebar.radio('What is the habitat?', ['Grasses', 'Leaves', 'Meadows', 'Paths', 'Urban', 'Waste', 'Woods'])


    # DATAFRAME
    # connecting the user input to the 96 columns
    user_input_dic = {
        # CAP SHAPE
        'cap_shape_b' : cap_shape_dict['Bell'],
        'cap_shape_c' : cap_shape_dict['Conical'],
        'cap_shape_f' : cap_shape_dict['Flat'],
        'cap_shape_k' : cap_shape_dict['Knobbed'],
        'cap_shape_s' : cap_shape_dict['Sunken'],
        'cap_shape_x' : cap_shape_dict['Convex'],
        # CAP SURFACE
        'cap_surface_f' : cap_surface_dict['Fibrous'],
        'cap_surface_g' : cap_surface_dict['Grooves'],
        'cap_surface_s' : cap_surface_dict['Scaly'],
        'cap_surface_y' : cap_surface_dict['Smooth'],
        # CAP COLOR
 
        
    }

    user_input_df = pd.DataFrame(user_input_dic, index=[0])
    return user_input_df