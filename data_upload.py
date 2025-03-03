import streamlit as st
import pandas as pd

def show():
    st.title("Upload Data")
    st.subheader("Upload your dataset")

    # File uploader
    file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

    if file:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        st.session_state['data'] = df  # Store the data in session state

        st.success("File uploaded successfully!")
        st.write("### Preview of the dataset:")
        st.dataframe(df.head())

        st.write(f"#### Rows: {df.shape[0]}, Columns: {df.shape[1]}")