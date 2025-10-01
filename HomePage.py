# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
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

# WELCOME PAGE TITLE
st.title("Welcome to the Data Dashboard!")
st.header("Anvita Kallam - Lab 2 - CS 1301")

# INTRODUCTORY TEXT
st.write("""
This application is designed to collect and visualize data.
You can navigate to the different pages using the sidebar on the left.

### How to use this app:
- **Survey Page**: Go here to input new data into our CSV file about what you do in your free time and how many hours you spend on it per week.
- **Visuals Page**: Go here to see the data visualized in different graphs.

This project is part of CS 1301's Lab 2.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
st.image("images/welcome_image.png")