import streamlit as st
from data_upload import show as show_upload
from data_exploration import show as show_explore
from value_counts import show as show_value_counts
from group_by import show as show_group_by
from visualizations import show as show_visualizations


# Setting Page Config
st.set_page_config(
    page_title="DataXplorer",
    page_icon="📊",
    layout="wide",
    # initial_sidebar_state="collapsed"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Upload Data", "Explore Data", "Value Counts", "Group By", "Visualizations"])

# Routing Pages
if page == "Upload Data":
    show_upload()
elif page == "Explore Data":
    show_explore()
elif page == "Value Counts":
    show_value_counts()
elif page == "Group By":
    show_group_by()
elif page == "Visualizations":
    show_visualizations()