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

    .stAlert > div[data-testid="alert"] {
        border-radius: 8px !important;
        border: 2px solid !important;
        font-weight: 500 !important;
    }
    
    .stAlert > div[data-testid="alert"]:has([data-testid="alert-warning"]) {
        background-color: #ffe6f0 !important;
        border-color: #ff66b2 !important;
        color: #8b2252 !important;
    }
    
    
    .stAlert > div[data-testid="alert"]:has([data-testid="alert-success"]) {
        background-color: #e6f7f4 !important;
        border-color: #28a745 !important;
        color: #155724 !important;
    }
    

    </style>
    """,
    unsafe_allow_html=True
)

# PAGE TITLE AND INFORMATION
st.title("Data Visualizations")
st.write("")
st.write("This page displays graphs based on the collected data. The data is based on your input to the survey, as well as a json file that contains music data regarding what songs and artists are my favorites.")


# DATA LOADING
# A crucial step is to load the data from the files.
# It's important to add error handling to prevent the app from crashing if a file is empty or missing.

st.divider()
st.header("Load Data")

# Load CSV with error handling
csv_df = None
if os.path.exists("data.csv") and os.path.getsize("data.csv") > 0:
    try:
        csv_df = pd.read_csv("data.csv")
        st.success("Loaded CSV from: data.csv")
        with st.expander("Preview CSV data"):
            st.dataframe(csv_df, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to read CSV: {e}")
else:
    st.warning("CSV file not found or empty. Add data from the Survey page.")

# Load JSON with error handling
json_df = None
if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            json_payload = json.load(f)
        
        if isinstance(json_payload, list):
            json_df = pd.DataFrame(json_payload)
        elif isinstance(json_payload, dict) and "data_points" in json_payload:
            json_df = pd.DataFrame(json_payload["data_points"])
        else:
            json_df = pd.DataFrame(json_payload)
        
        st.success("Loaded JSON from: data.json")
        with st.expander("Preview JSON data"):
            st.dataframe(json_df, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to read JSON: {e}")
else:
    st.warning("JSON file not found or empty.")


# GRAPH CREATION
# The lab requires you to create 3 graphs: one static and two dynamic.
# You must use both the CSV and JSON data sources at least once.

st.divider()
st.header("Graphs")

# GRAPH 1: STATIC
st.subheader("Graph 1: Top Ratings (Static - JSON Data)")
st.warning("This graph shows the top 10 songs by overall rating.")
if json_df is not None and {"Song", "Overall Rating"}.issubset(json_df.columns):
    json_top = (
        json_df[["Song", "Overall Rating"]]
        .sort_values("Overall Rating", ascending=False)
        .head(10)
        .set_index("Song")
    )
    st.bar_chart(json_top["Overall Rating"])
else:
    st.info("JSON data not available or missing required columns.")

# GRAPH 2: DYNAMIC (CSV)
st.subheader("Graph 2: CSV Filtered Values (Dynamic - CSV Data)")
st.warning("This graph shows the relationship between the category and the value of the data.")
if csv_df is not None and not csv_df.empty:
    col_a, col_b = st.columns(2)
    with col_a:
        min_value = st.slider("Minimum Value", 0, 100, 0)
    with col_b:
        category_query = st.text_input("Category contains…", "")

    filtered_df = csv_df.copy()
    category_col = "Category" if "Category" in filtered_df.columns else filtered_df.columns[0]
    value_col = "Value" if "Value" in filtered_df.columns else (
        filtered_df.columns[1] if len(filtered_df.columns) > 1 else filtered_df.columns[0]
    )
    filtered_df[value_col] = pd.to_numeric(filtered_df[value_col], errors="coerce")
    filtered_df = filtered_df.dropna(subset=[value_col])

    if category_query:
        filtered_df = filtered_df[
            filtered_df[category_col].astype(str).str.contains(category_query, case=False, na=False)
        ]
    filtered_df = filtered_df[filtered_df[value_col] >= min_value]
    
    if not filtered_df.empty:
        st.line_chart(filtered_df.set_index(category_col)[value_col])
    else:
        st.info("No data matches the current filters.")
else:
    st.info("CSV data not available. Add data from the Survey page.")

# GRAPH 3: DYNAMIC (JSON)
st.subheader("Graph 3: Energy vs Lyrics Impact (Dynamic - JSON Data)")
st.warning("This graph shows the relationship between the energy level of a song and the impact of the lyrics on the overall rating of the song.")
if json_df is not None and {"Artist", "Genre", "Mood Fit", "Energy Level", "Lyrics Impact"}.issubset(json_df.columns):
    group_by = st.selectbox("Group by", ["Artist", "Genre"], index=0)
    mood_options = sorted(json_df["Mood Fit"].dropna().unique().tolist())
    moods = st.multiselect("Filter moods", mood_options, default=[])

    df3 = json_df.copy()
    if moods:
        df3 = df3[df3["Mood Fit"].isin(moods)]

    for col in ["Energy Level", "Lyrics Impact", "Overall Rating"]:
        df3[col] = pd.to_numeric(df3[col], errors="coerce")
    df3 = df3.dropna(subset=["Energy Level", "Lyrics Impact"]).copy()

    if not df3.empty:
        st.scatter_chart(df3, x="Energy Level", y="Lyrics Impact")
        summary = (
            df3.groupby(group_by)[["Energy Level", "Lyrics Impact", "Overall Rating"]]
            .mean(numeric_only=True)
            .sort_values("Overall Rating", ascending=False)
        )
        with st.expander("Group summary (averages)"):
            st.dataframe(summary, use_container_width=True)
    else:
        st.info("No data points to display for the current filters.")
else:
    st.info("JSON data not available or missing required columns.")
