# This creates the page for displaying data visualizations.
# It should read data from both 'data.csv' and 'data.json' to create graphs.

import streamlit as st
import pandas as pd
import json # The 'json' module is needed to work with JSON files.
import os   # The 'os' module helps with file system operations.

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visualizations",
    page_icon="📈",
)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #b2d8d8 0%, #008080 50%, #006666 100%);
        color: #ffe6f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    h1, h2, h3, h4 {
        color: #66b2b2;
        font-weight: 600;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    h1 {
        color: #b2d8d8;
        border-bottom: 3px solid #ff66b2;
        padding-bottom: 10px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #b2d8d8 0%, #008080 100%);
        color: #ffe6f0;
        border-right: 2px solid #ff66b2;
    }

    section[data-testid="stSidebar"] a {
        color: #b2d8d8 !important;
        font-weight: 500;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    section[data-testid="stSidebar"] a:hover {
        color: #ff99cc !important;
    }


    div[data-baseweb="tab"] {
        background: rgba(45, 27, 45, 0.6);
        color: #ffe6f0;
        font-weight: 500;
        border: 1px solid rgba(255, 153, 204, 0.3);
        border-radius: 8px 8px 0 0;
        transition: all 0.3s ease;
    }
    div[data-baseweb="tab"]:hover {
        background: rgba(255, 102, 178, 0.1);
        color: #b2d8d8;
        border-color: #b2d8d8;
    }
    div[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #b2d8d8, #006666);
        color: white;
        border-color: #b2d8d8;
    }

    .stProgress > div > div {
        background: linear-gradient(90deg, #b2d8d8, #006666);
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(255, 102, 178, 0.3);
    }


    .stMarkdown {
        color: #ffe6f0;
    }

    .stImage > img {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        border: 2px solid rgba(255, 153, 204, 0.3);
    }

    .stSidebar .stText {
        color: #ffe6f0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations 📈")
st.write("This page displays graphs based on the collected data.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# TO DO:
# 1. Load the data from 'data.csv' into a pandas DataFrame.
#    - Use a 'try-except' block or 'os.path.exists' to handle cases where the file doesn't exist.
# 2. Load the data from 'data.json' into a Python dictionary.
#    - Use a 'try-except' block here as well.

st.info("TODO: Add your data loading logic here.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC GRAPH
st.subheader("Graph 1: Static") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create a static graph (e.g., bar chart, line chart) using st.bar_chart() or st.line_chart().
# - Use data from either the CSV or JSON file.
# - Write a description explaining what the graph shows.
st.warning("Placeholder for your first graph.")


# GRAPH 2: DYNAMIC GRAPH
st.subheader("Graph 2: Dynamic") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TODO:
# - Create a dynamic graph that changes based on user input.
# - Use at least one interactive widget (e.g., st.slider, st.selectbox, st.multiselect).
# - Use Streamlit's Session State (st.session_state) to manage the interaction.
# - Add a '#NEW' comment next to at least 3 new Streamlit functions you use in this lab.
# - Write a description explaining the graph and how to interact with it.
st.warning("Placeholder for your second graph.")


# GRAPH 3: DYNAMIC GRAPH
st.subheader("Graph 3: Dynamic") # CHANGE THIS TO THE TITLE OF YOUR GRAPH
# TO DO:
# - Create another dynamic graph.
# - If you used CSV data for Graph 1 & 2, you MUST use JSON data here (or vice-versa).
# - This graph must also be interactive and use Session State.
# - Remember to add a description and use '#NEW' comments.
st.warning("Placeholder for your third graph.")
