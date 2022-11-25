import pandas as pd
import numpy as np

# DEPLOYMENT
import streamlit as st

# PLOTTING
import matplotlib.pyplot as plt
#set a global label font size for all plots
plt.rc('font', size=10)
plot_colours = ['lightgreen', 'mediumturquoise', 'deepskyblue', 'cornflowerblue','mediumpurple','mediumorchid','mediumvioletred']
# seaborn and global settings
import seaborn as sns
sns.axes_style("white")
# set global pallette
sns.set_palette(sns.color_palette(plot_colours))
# 3D plotting
from mpl_toolkits.mplot3d import Axes3D

# TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split

# MODELS 
from sklearn.cluster import KMeans, k_means

# PREPROCESSING
from sklearn.preprocessing import scale ,StandardScaler
from sklearn.preprocessing import LabelEncoder

# POST PROCESSING
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# METRICS
import sklearn.metrics as sm
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report

#--------------------------------------------------
# IMPORT DATA
#--------------------------------------------------
original_df = pd.read_csv('final_original_df.csv')
# remove the null values from the original database 
original_df.dropna(inplace=True)
# dummied database
dummied_df = pd.read_csv('final_dummies_df.csv')

#--------------------------------------------------
# APP DETAILS
#--------------------------------------------------
st.title('Unsupervised Learning Assignment')
st.subheader('K-Means Clustering on Customer Dataset')

# adding tabs to the main page to separate my information
m_tab1, m_tab2, m_tab3 = st.tabs(['Dataset Preview', 'Data Preprocessing', 'Model'])

# TAB 1 - DATASET PREVIEW
with m_tab1:
    st.header('Dataset Preview')
    st.write('Analysing the dataset using charts.')
    st.write('The dataset contains information about customers of a car dealership.')
    # separating the information into columns
    tab1_col1, tab1_col2 = st.columns(2) 
    # COLUMN 1
    with tab1_col1:
        st.image('gender.png', width=300)
        st.image('ever_married.png', width=300)
        st.image('age.png', width=300)
        st.image('graduated.png', width=300)

     # COLUMN 2
    with tab1_col2:
        st.image('profession.png', width=300)
        st.image('work_experience.png', width=300)
        st.image('spending_score.png', width=300)
        st.image('family_size.png', width=300)

# TAB 2 - DATA PREPROCESSING

# TAB 3 - MODEL
with m_tab3:
    st.header('Model')
    st.write('Applying K-Means Clustering to the dataset.')
    st.write('Displyaing the results using PCA')
    st.write('These three principal components control  42.86 % of the variance in the dataset.')
    st.write('')
    st.image('final_inertia_elbow.png', width=None)
    st.image('pca_2_components.png', width=None)
    st.image('pca_3_components.png', width=None) 
