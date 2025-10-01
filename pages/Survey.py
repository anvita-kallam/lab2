# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
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

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey - Free Time")
st.write("")
st.write("Please fill out the form below to add your data to the dataset. Add whatever you do in your free time and how many hours you spend on it per week! This is a chance to get to know yourself better and see what you spend your time on.")
st.image("images/activity_image.png")
# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.text_input("What do you do in your free time?:")
    value_input = st.text_input("Hours per Week:")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        csv_path = 'data.csv'
        with open(csv_path, 'a', newline='\n', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([category_input, value_input])
        
        st.success("Your data has been submitted!")
        st.write(f"You entered: **Category:** {category_input}, **Value:** {value_input}")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")