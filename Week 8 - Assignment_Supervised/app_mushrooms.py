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
st.title('Mushroom Edibility Classifier')
page1_tab1, page1_tab2 = st.tabs(['Enter Data', 'Data Summary'])

with page1_tab1:
    # mushroom data tabs
    cap_tab, gill_tab, stalk_tab, veil_tab, rings_tab, other_tab = st.tabs(["Cap", "Gill", "Stalk", "Veil", "Rings", "Other"])
    # columns within the tabs that hold all the user inputs for the mushroom data
    cap_column1, cap_column2 = cap_tab.columns(2) #CAP
    gill_column1, gill_column2 = gill_tab.columns(2) #GILL
    stalk_column1, stalk_column2, stalk_column3 = stalk_tab.columns(3) #STALK
    other_column1, other_column2 = other_tab.columns(2) #OTHER


with page1_tab2:
    # summary of the users input is in this tab
    st.header('Mushroom Data Summary')
    # this container shows the results of the user input that is generated at the end of the code
    results_container = st.container()
    # this container is here so the user data us displayed under the results
    data_summary_container = st.container()
    with data_summary_container:
        data_summary_column1, data_summary_column2, data_summary_column3 = st.columns([1.25,1.5,1])


# SIDEBAR
st.sidebar.image('mushrooms.jpg', width=300)


#---------------------------------
# USER INPUT
#---------------------------------

def user_input():

    # nearly every radio button below has an associated dictionary that will be used to map the user input to the correct value for the model
    # ie 0 or 1 
    # this function will be called after the user makes a selection and it will update the dictionary with the correct value
    def assign_dict(parameter, dictionary):
        for i in dictionary:
            # if the user has selected 'Bell' this will be passed through and the dictionary will update 'Bell' to 1 and the rest of the values to 0
            # this is important because there can only be one answer for each parameter
            if i == parameter:
                dictionary[i] = 1
            else:
                dictionary[i] = 0

    # CAP TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with cap_tab:
        with cap_column1:
    # CAP SHAPE ***********************************************************
        # bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
    # Dictionary - Cap Shape
            cap_shape_dict = {'Bell': 0, 'Conical': 0, 'Flat': 0, 'Knobbed': 0, 'Sunken': 0, 'Convex': 0}
            cap_shapes = list(cap_shape_dict.keys())
    # Radio Button - Cap Shape
            cap_shape = st.radio('What is the cap shape?', cap_shapes)
    # update the dictionary with the users input 
            assign_dict(cap_shape, cap_shape_dict)

           
    # CAP SURFACE *******************************************************
        # fibrous=f, grooves=g, scaly=y, smooth=s
    # Dictionary - Cap Surface
            cap_surface_dict = {'Fibrous': 0, 'Grooves': 0, 'Smooth': 0, 'Scaly': 0}
            cap_surfaces = list(cap_surface_dict.keys())
    # Radio Button - Cap Surface
            cap_surface = st.radio('What is the cap surface?', cap_surfaces)
    # update the dictionary with the users input
            assign_dict(cap_surface, cap_surface_dict)

        with cap_column2:
    # CAP COLOR **********************************************************
        # brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
    # Dictionary - Cap Color
            cap_color_dict = {'Brown': 0, 'Buff': 0, 'Cinnamon': 0, 'Gray': 0, 'Green': 0, 'Pink': 0, 'Purple': 0, 'Red': 0, 'White': 0, 'Yellow': 0}
            cap_colors = list(cap_color_dict.keys())
    # Radio Button - Cap Color
            cap_color = st.radio('What is the cap color?', cap_colors)
    # update the dictionary with the users input
            assign_dict(cap_color, cap_color_dict)
    

    # GILL TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with gill_tab:
        with gill_column1:
    # GILL ATTACHMENT **************************************************
        # attached=a,free=f, 
    # Dictionary - Gill Attachment
            gill_attachment_dict = {'Attached': 0, 'Free': 0}
            gill_attachments = list(gill_attachment_dict.keys())
    # Radio Button - Gill Attachment
            gill_attachment = st.radio('How is the gill attatched?', gill_attachments)
    # update the dictionary with the users input
            assign_dict(gill_attachment, gill_attachment_dict)


    # GILL SPACING *****************************************************
        # close=c, crowded=w
    # Dictionary - Gill Spacing
            gill_spacing_dict = {'Close': 0, 'Crowded': 0}
            gill_spacings = list(gill_spacing_dict.keys())
    # Radio Button - Gill Spacing
            gill_spacing = st.radio('What is the gill spacing?', gill_spacings)
    # update the dictionary with the users input
            assign_dict(gill_spacing, gill_spacing_dict)


    # GILL SIZE ********************************************************
        # broad=b, narrow=n
    # Dictionary - Gill Size
            gill_size_dict = {'Broad': 0, 'Narrow': 0}
            gill_sizes = list(gill_size_dict.keys())
    # Radio Button - Gill Size
            gill_size = st.radio('What is the gill size?', gill_sizes)
    # update the dictionary with the users input
            assign_dict(gill_size, gill_size_dict)

        with gill_column2:
    # GILL COLOR ********************************************************
        # black=k, brown=n, buff=b, chocolate=h, gray=g, green=r, orange=o, pink=p, purple=u, red=e, white=w, yellow=y
    # Dictionary - Gill Color
            gill_color_dict = {'Black': 0, 'Brown': 0, 'Buff': 0, 'Chocolate': 0, 'Gray': 0, 'Green': 0, 'Orange': 0, 'Pink': 0, 'Purple': 0, 'Red': 0, 'White': 0, 'Yellow': 0}
            gill_colors = list(gill_color_dict.keys())
    # Radio Button - Gill Color
            gill_color = st.radio('What is the gill color?', gill_colors)
    # update the dictionary with the users input
            assign_dict(gill_color, gill_color_dict)



    # CAP TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with stalk_tab:
        with stalk_column1:
            stalk_column1.write('Whole Stalk')
    # STALK SHAPE *******************************************************
        # enlarging=e, tapering=t
    # Dictionary - Stalk Shape
            stalk_shape_dict = {'Enlarging': 0, 'Tapering': 0}
            stalk_shapes = list(stalk_shape_dict.keys())
    # Radio Button - Stalk Shape
            stalk_shape = st.radio('What is the stalk shape?', stalk_shapes)
    # update the dictionary with the users input
            assign_dict(stalk_shape, stalk_shape_dict)


    # STALK ROOT ********************************************************
        # bulbous=b, club=c, equal=e, rooted=r, missing=? 
    # Dictionary - Stalk Root
            stalk_root_dict = {'Bulbous': 0, 'Club': 0, 'Equal': 0, 'Rooted': 0, 'Missing': 0}
            stalk_roots = list(stalk_root_dict.keys())
    # Radio Button - Stalk Root
            stalk_root = st.radio('What is the stalk root?', stalk_roots)
    # update the dictionary with the users input
            assign_dict(stalk_root, stalk_root_dict)


        with stalk_column2:
            stalk_column2.write('Above Ring')
    # STALK SURFACE ABOVE RING ******************************************
        # fibrous=f, scaly=y, silky=k, smooth=s
    # Dictionary - Stalk Surface Above Ring
            stalk_surface_above_ring_dict = {'Fibrous': 0, 'Scaly': 0, 'Silky': 0, 'Smooth': 0}
            stalk_surface_above_rings = list(stalk_surface_above_ring_dict.keys())
    # Radio Button - Stalk Surface Above Ring
            stalk_surface_above_ring = st.radio('Describe the stalk surface above the ring?', stalk_surface_above_rings)
    # update the dictionary with the users input
            assign_dict(stalk_surface_above_ring, stalk_surface_above_ring_dict)


    # STALK COLOR ABOVE RING ********************************************
        # brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
    # Dictionary - Stalk Color Above Ring
            stalk_color_above_ring_dict = {'Brown': 0, 'Buff': 0, 'Cinnamon': 0, 'Gray': 0, 'Orange': 0, 'Pink': 0, 'Red': 0, 'White': 0, 'Yellow': 0}
            stalk_color_above_rings = list(stalk_color_above_ring_dict.keys())
    # Radio Button - Stalk Color Above Ring
            stalk_color_above_ring = st.radio('What is the stalk color above ring?', stalk_color_above_rings)
    # update the dictionary with the users input
            assign_dict(stalk_color_above_ring, stalk_color_above_ring_dict)


        with stalk_column3:
            stalk_column3.write('Below Ring')
    # STALK SURFACE BELOW RING ******************************************
        # fibrous=f, scaly=y, silky=k, smooth=s
    # Dictionary - Stalk Surface Below Ring
            stalk_surface_below_ring_dict = {'Fibrous': 0, 'Scaly': 0, 'Silky': 0, 'Smooth': 0}
            stalk_surface_below_rings = list(stalk_surface_below_ring_dict.keys())
    # Radio Button - Stalk Surface Below Ring
            stalk_surface_below_ring = st.radio('Describe the stalk surface below the ring?', stalk_surface_below_rings)
    # update the dictionary with the users input
            assign_dict(stalk_surface_below_ring, stalk_surface_below_ring_dict)


    # STALK COLOR BELOW RING ********************************************
        # brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
    # Dictionary - Stalk Color Below Ring
            stalk_color_below_ring_dict = {'Brown': 0, 'Buff': 0, 'Cinnamon': 0, 'Gray': 0, 'Orange': 0, 'Pink': 0, 'Red': 0, 'White': 0, 'Yellow': 0}
            stalk_color_below_rings = list(stalk_color_below_ring_dict.keys())
    # Radio Button - Stalk Color Below Ring
            stalk_color_below_ring = st.radio('What is the stalk color below ring?', stalk_color_below_rings)
    # update the dictionary with the users input
            assign_dict(stalk_color_below_ring, stalk_color_below_ring_dict)


    # VEIL TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with veil_tab:
    # VEIL TYPE *********************************************************
        # partial=p, universal=u
        veil_type = st.radio('What is the veil type partial?', ['Yes', 'No'])
    # there is only one column for veil type, so I cant use the dictionary method instead I can just assign the value as 0 or 1
        if veil_type == 'Yes':
            veil_type = 1 # partial
        else:
            veil_type = 0 # universal


    # VEIL COLOR ********************************************************
        # brown=n, orange=o, white=w, yellow=y
    # Dictionary - Veil Color
        veil_color_dict = {'Brown': 0, 'Orange': 0, 'White': 0, 'Yellow': 0}
        veil_colors = list(veil_color_dict.keys())
    # Radio Button - Veil Color
        veil_color = st.radio('What is the veil color?', veil_colors)
    # update the dictionary with the users input
        assign_dict(veil_color, veil_color_dict)

    # RING TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with rings_tab:
    # RING NUMBER *******************************************************
        # none=n, one=o, two=t
    # Dictionary - Ring Number
        ring_number_dict = {'None': 0, 'One': 0, 'Two': 0}
        ring_numbers = list(ring_number_dict.keys())
    # Radio Button - Ring Number
        ring_number = st.radio('How many rings are there?', ring_numbers)
    # update the dictionary with the users input
        assign_dict(ring_number, ring_number_dict)


    # RING TYPE *********************************************************
        # evanescent=e, flaring=f, large=l, none=n, pendant=p
    # Dictionary - Ring Type
        ring_type_dict = {'Evanescent': 0, 'Flaring': 0, 'Large': 0, 'None': 0, 'Pendant': 0}
        ring_types = list(ring_type_dict.keys())
    # Radio Button - Ring Type
        ring_type = st.radio('What is the ring type?', ring_types)
    # update the dictionary with the users input
        assign_dict(ring_type, ring_type_dict)

    # OTHER TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with other_tab:
        with other_column1:
    # BRUISES ***********************************************************
        # bruises=t, no=f
    # Dictionary - Bruises
            bruises_dict = {'Yes': 0, 'No': 0}
            bruises = list(bruises_dict.keys())
    # Radio Button - Bruises
            bruise_answer = st.radio('Does it bruise?', bruises)
    # update the dictionary with the users input
            assign_dict(bruise_answer, bruises_dict)


    # POPULATION ********************************************************
        # abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
    # Dictionary - Population
            population_dict = {'Abundant': 0, 'Clustered': 0, 'Numerous': 0, 'Scattered': 0, 'Several': 0, 'Solitary': 0}
            populations = list(population_dict.keys())
    # Radio Button - Population
            population = st.radio('What is the population?', populations)
    # update the dictionary with the users input
            assign_dict(population, population_dict)


    # HABITAT ***********************************************************
        # grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
    # Dictionary - Habitat
            habitat_dict = {'Grasses': 0, 'Leaves': 0, 'Meadows': 0, 'Paths': 0, 'Urban': 0, 'Waste': 0, 'Woods': 0}
            habitats = list(habitat_dict.keys())
    # Radio Button - Habitat
            habitat = st.radio('What is the habitat?', habitats)
    # update the dictionary with the users input
            assign_dict(habitat, habitat_dict)

            
        with other_column2:
    # ODOR *************************************************************
        # almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
    # Dictionary - Odor
            odor_dict = {'Almond': 0, 'Anise': 0, 'Creosote': 0, 'Fishy': 0, 'Foul': 0, 'Musty': 0, 'Pungent': 0, 'Spicy': 0, 'None': 0}
            odors = list(odor_dict.keys())
    # Radio Button - Odor
            odor = st.radio('What is the odor?', odors)
    # update the dictionary with the users input
            assign_dict(odor, odor_dict)


    # SPORE PRINT COLOR *************************************************
        # black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
    # Dictionary - Spore Print Color
            spore_print_color_dict = {'Black': 0, 'Brown': 0, 'Buff': 0, 'Chocolate': 0, 'Green': 0, 'Orange': 0, 'Purple': 0, 'White': 0, 'Yellow': 0}
            spore_print_colors = list(spore_print_color_dict.keys())
    # Radio Button - Spore Print Color
            spore_print_color = st.radio('What is the spore print color?', spore_print_colors)
    # update the dictionary with the users input
            assign_dict(spore_print_color, spore_print_color_dict)

    # SUMMARY TAB ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    with page1_tab2:
        with data_summary_column1:

            st.subheader('Cap')  
            st.write('__Cap Shape:__ ', cap_shape)
            st.write('__Cap Surface:__ ', cap_surface)
            st.write('__Cap Color:__ ', cap_color) 

            st.subheader('Gill')
            st.write('__Gill Attachment:__ ', gill_attachment)
            st.write('__Gill Spacing:__ ', gill_spacing)
            st.write('__Gill Size:__ ', gill_size)
            st.write('__Gill Color:__ ', gill_color)

        with data_summary_column2:
            st.subheader('Stalk')
            st.write('__Stalk Shape:__ ', stalk_shape)
            st.write('__Stalk Root:__ ', stalk_root)
            st.write('__Stalk Surface Above Ring:__ ', stalk_surface_above_ring)
            st.write('__Stalk Surface Below Ring:__ ', stalk_surface_below_ring)
            st.write('__Stalk Color Above Ring:__ ', stalk_color_above_ring)
            st.write('__Stalk Color Below Ring:__ ', stalk_color_below_ring)

            st.subheader('Veil')
            if veil_type == 'Yes':
                st.write('__Veil Type:__ Partial')
            else:
                st.write('__Veil Type:__ Universal') 
            st.write('__Veil Color:__ ', veil_color)

        with data_summary_column3:
            st.subheader('Ring')
            st.write('__Ring Number:__ ', ring_number)
            st.write('__Ring Type:__ ', ring_type)

            st.subheader('Other')
            st.write('__Bruises:__ ', bruise_answer)
            st.write('__Population:__ ', population)
            st.write('__Habitat:__ ', habitat)
            st.write('__Odor:__ ', odor)
            st.write('__Spore Print Color:__ ', spore_print_color)


    # DATAFRAME +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # connecting the user input to the 118 columns
    user_input_dic = {
        # CAP SHAPE COLUMNS
        'cap_shape_b' : cap_shape_dict['Bell'],
        'cap_shape_c' : cap_shape_dict['Conical'],
        'cap_shape_f' : cap_shape_dict['Flat'],
        'cap_shape_k' : cap_shape_dict['Knobbed'],
        'cap_shape_s' : cap_shape_dict['Sunken'],
        'cap_shape_x' : cap_shape_dict['Convex'],
        # CAP SURFACE COLUMNS
        'cap_surface_f' : cap_surface_dict['Fibrous'],
        'cap_surface_g' : cap_surface_dict['Grooves'],
        'cap_surface_s' : cap_surface_dict['Smooth'],
        'cap_surface_y' : cap_surface_dict['Scaly'],
        # CAP COLOR COLUMNS
        'cap_color_b' : cap_color_dict['Brown'],
        'cap_color_c' : cap_color_dict['Cinnamon'],
        'cap_color_e' : cap_color_dict['Red'],
        'cap_color_g' : cap_color_dict['Gray'],
        'cap_color_n' : cap_color_dict['Buff'],
        'cap_color_p' : cap_color_dict['Pink'],
        'cap_color_r' : cap_color_dict['Green'],
        'cap_color_u' : cap_color_dict['Purple'],
        'cap_color_w' : cap_color_dict['White'],
        'cap_color_y' : cap_color_dict['Yellow'],
        # BRUISES COLUMNS
        'bruises_f' : bruises_dict['No'],
        'bruises_t' : bruises_dict['Yes'],
        # ODOR COLUMNS
        'odor_a' : odor_dict['Almond'],
        'odor_c' : odor_dict['Creosote'],
        'odor_f' : odor_dict['Foul'],
        'odor_l' : odor_dict['Fishy'],
        'odor_m' : odor_dict['Musty'],
        'odor_n' : odor_dict['None'],
        'odor_p' : odor_dict['Pungent'],
        'odor_s' : odor_dict['Spicy'],
        'odor_y' : odor_dict['Anise'],
        # GILL ATTACHMENT COLUMNS
        'gill_attachment_a' : gill_attachment_dict['Attached'],
        'gill_attachment_f' : gill_attachment_dict['Free'],
        # GILL SPACING COLUMNS
        'gill_spacing_c' : gill_spacing_dict['Close'],
        'gill_spacing_w' : gill_spacing_dict['Crowded'],
        # GILL SIZE COLUMNS
        'gill_size_b' : gill_size_dict['Broad'],
        'gill_size_n' : gill_size_dict['Narrow'],
        # GILL COLOR COLUMNS
        'gill_color_b' : gill_color_dict['Black'],
        'gill_color_e' : gill_color_dict['Brown'],
        'gill_color_g' : gill_color_dict['Buff'],
        'gill_color_h' : gill_color_dict['Chocolate'],
        'gill_color_k' : gill_color_dict['Orange'],
        'gill_color_n' : gill_color_dict['Pink'],
        'gill_color_o' : gill_color_dict['Purple'],
        'gill_color_p' : gill_color_dict['Red'],
        'gill_color_r' : gill_color_dict['Green'],
        'gill_color_u' : gill_color_dict['White'],
        'gill_color_w' : gill_color_dict['Yellow'],
        'gill_color_y' : gill_color_dict['Gray'],
        # STALK SHAPE COLUMNS
        'stalk_shape_e' : stalk_shape_dict['Enlarging'],
        'stalk_shape_t' : stalk_shape_dict['Tapering'],
        # STALK ROOT COLUMNS
        'stalk_root_b' : stalk_root_dict['Bulbous'],
        'stalk_root_c' : stalk_root_dict['Club'],
        'stalk_root_e' : stalk_root_dict['Equal'],
        'stalk_root_r' : stalk_root_dict['Rooted'],
        'stalk_root_z' : stalk_root_dict['Missing'],
        # STALK SURFACE ABOVE RING COLUMNS
        'stalk_surface_above_ring_f' : stalk_surface_above_ring_dict['Fibrous'],
        'stalk_surface_above_ring_k' : stalk_surface_above_ring_dict['Silky'],
        'stalk_surface_above_ring_s' : stalk_surface_above_ring_dict['Scaly'],
        'stalk_surface_above_ring_y' : stalk_surface_above_ring_dict['Smooth'],
        # STALK SURFACE BELOW RING COLUMNS
        'stalk_surface_below_ring_f' : stalk_surface_below_ring_dict['Fibrous'],
        'stalk_surface_below_ring_k' : stalk_surface_below_ring_dict['Silky'],
        'stalk_surface_below_ring_s' : stalk_surface_below_ring_dict['Scaly'],
        'stalk_surface_below_ring_y' : stalk_surface_below_ring_dict['Smooth'],
        # STALK COLOR ABOVE RING COLUMNS
        'stalk_color_above_ring_b' : stalk_color_above_ring_dict['Brown'],
        'stalk_color_above_ring_c' : stalk_color_above_ring_dict['Cinnamon'],
        'stalk_color_above_ring_e' : stalk_color_above_ring_dict['Red'],
        'stalk_color_above_ring_g' : stalk_color_above_ring_dict['Gray'],
        'stalk_color_above_ring_n' : stalk_color_above_ring_dict['Buff'],
        'stalk_color_above_ring_o' : stalk_color_above_ring_dict['Orange'],
        'stalk_color_above_ring_p' : stalk_color_above_ring_dict['Pink'],
        'stalk_color_above_ring_w' : stalk_color_above_ring_dict['White'],
        'stalk_color_above_ring_y' : stalk_color_above_ring_dict['Yellow'],
        # STALK COLOR BELOW RING COLUMNS
        'stalk_color_below_ring_b' : stalk_color_below_ring_dict['Brown'],
        'stalk_color_below_ring_c' : stalk_color_below_ring_dict['Cinnamon'],
        'stalk_color_below_ring_e' : stalk_color_below_ring_dict['Red'],
        'stalk_color_below_ring_g' : stalk_color_below_ring_dict['Gray'],
        'stalk_color_below_ring_n' : stalk_color_below_ring_dict['Buff'],
        'stalk_color_below_ring_o' : stalk_color_below_ring_dict['Orange'],
        'stalk_color_below_ring_p' : stalk_color_below_ring_dict['Pink'],
        'stalk_color_below_ring_w' : stalk_color_below_ring_dict['White'],
        'stalk_color_below_ring_y' : stalk_color_below_ring_dict['Yellow'],
        # VEIL TYPE COLUMNS
        'veil_type_p' : veil_type,
        # VEIL COLOR COLUMNS
        'veil_color_n' : veil_color_dict['Brown'],
        'veil_color_o' : veil_color_dict['Orange'],
        'veil_color_w' : veil_color_dict['White'],
        'veil_color_y' : veil_color_dict['Yellow'],
        # RING NUMBER COLUMNS
        'ring_number_n' : ring_number_dict['None'],
        'ring_number_o' : ring_number_dict['One'],
        'ring_number_t' : ring_number_dict['Two'],
        # RING TYPE COLUMNS
        'ring_type_e' : ring_type_dict['Evanescent'],
        'ring_type_f' : ring_type_dict['Flaring'],
        'ring_type_l' : ring_type_dict['Large'],
        'ring_type_n' : ring_type_dict['None'],
        'ring_type_p' : ring_type_dict['Pendant'],
        # SPORE PRINT COLOR COLUMNS
        'spore_print_color_b' : spore_print_color_dict['Black'],
        'spore_print_color_h' : spore_print_color_dict['Brown'],
        'spore_print_color_k' : spore_print_color_dict['Chocolate'],
        'spore_print_color_n' : spore_print_color_dict['Green'],
        'spore_print_color_o' : spore_print_color_dict['Orange'],
        'spore_print_color_r' : spore_print_color_dict['Purple'],
        'spore_print_color_u' : spore_print_color_dict['White'],
        'spore_print_color_w' : spore_print_color_dict['Yellow'],
        'spore_print_color_y' : spore_print_color_dict['Buff'],
        # POPULATION COLUMNS
        'population_a' : population_dict['Abundant'],
        'population_c' : population_dict['Clustered'],
        'population_n' : population_dict['Numerous'],
        'population_s' : population_dict['Scattered'],
        'population_v' : population_dict['Several'],
        'population_y' : population_dict['Solitary'],
        # HABITAT COLUMNS
        'habitat_g' : habitat_dict['Grasses'],
        'habitat_l' : habitat_dict['Leaves'],
        'habitat_m' : habitat_dict['Meadows'],
        'habitat_p' : habitat_dict['Paths'],
        'habitat_u' : habitat_dict['Urban'],
        'habitat_w' : habitat_dict['Waste'],
        'habitat_d' : habitat_dict['Woods']       
    }

    user_input_df = pd.DataFrame(user_input_dic, index=[0])
    return user_input_df

# --------------------------------------------
# Store the user input
# --------------------------------------------
user_data = user_input()


# --------------------------------------------
# MODEL
# --------------------------------------------
# DATA SPLITTING
X = df.drop('class_p', axis=1)
y = df['class_p']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# DECISION TREE CLASSIFIER
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

#PREDECTION
y_pred = clf.predict(user_data) 

#---------------------------------------------
# Display the results
#---------------------------------------------
st.sidebar.header('Results:')

if y_pred == 1:
    output = 'This 🍄 mushroom is poisonous. ☠️'
elif y_pred == 0:
    output = 'This 🍄 mushroom is not poisonous. 🫠'
else:
    output = 'Some thing has gone wrong. 😬 Oops.'

st.sidebar.subheader(output)
with results_container:
    st.subheader(output)