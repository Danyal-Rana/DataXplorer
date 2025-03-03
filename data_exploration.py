import streamlit as st
import pandas as pd

def show():
    st.title("Explore Data")
    st.subheader("Basic Information about the Dataset")

    # Check if data is uploaded
    if 'data' not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state['data']

    tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Top & Bottom Rows", "Data Types", "Columns"])

    with tab1:
        st.write(f"There are {df.shape[0]} rows and {df.shape[1]} columns in the dataset.")
        st.subheader("Summary Statistics")
        st.dataframe(df.describe())

    with tab2:
        st.subheader("Top Rows")
        top_rows = st.slider("Select Number of Top Rows", 1, df.shape[0], 5)
        st.dataframe(df.head(top_rows))

        st.subheader("Bottom Rows")
        bottom_rows = st.slider("Select Number of Bottom Rows", 1, df.shape[0], 5)
        st.dataframe(df.tail(bottom_rows))

    with tab3:
        st.subheader("Data Types of Columns")
        st.dataframe(df.dtypes)

    with tab4:
        st.subheader("Columns in Dataset")
        st.write(list(df.columns))