import streamlit as st
import pandas as pd 
import numpy as np

st.sidebar.title("SAPGrafici")

uploaded_file = st.sidebar.file_uploader("Upload excel file:")
if uploaded_file is not None:

    dataframe = pd.read_excel(uploaded_file)
    st.title("Dashboard")
    
    list = dataframe.columns.values
    list = np.delete(list, [0,1,2], 0)

    selectedAppServer = st.sidebar.selectbox('Selected Application Server',dataframe['Application Server Instance'].unique())
    selectedValueGraphics = st.sidebar.selectbox('Select value to calculate chart',list)
    
    #Filter pandas dataframe to obtain clean table
    dfSelAppServer = dataframe[dataframe['Application Server Instance'] == selectedAppServer]
    dfSelAppServer = dfSelAppServer[['Time', 'Application Server Instance', selectedValueGraphics]]
    dfSelAppServer['Time'] = '10 Oct 2011 ' + dfSelAppServer['Time'].astype(str)

    #Plot result on vega lite chart
    st.vega_lite_chart(dfSelAppServer, {
    "width": 1000,
    "autosize": {
    "type": "fit",
    "contains": "padding"
    },
    "height": 400,
    "mark": "bar",
    "encoding": {
        "x": {
            "timeUnit": "hoursminutesseconds",
            "field": "Time",
            "type": "ordinal",
            "title": "Time",
        },
        "y": {
            "field": selectedValueGraphics,
            "type": "quantitative",
            "title": selectedValueGraphics, 
        },
    },
    })
