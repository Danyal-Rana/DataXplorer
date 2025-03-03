import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Value Counts")
    st.subheader("Analyze the Frequency of Values in a Column")

    # Check if data is uploaded
    if 'data' not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state['data']

    with st.expander("Value Count Analysis"):
        col1, col2 = st.columns(2)

        with col1:
            column = st.selectbox("Select Column", options=list(df.columns))

        with col2:
            num_values = st.number_input("Number of Values to Show", min_value=1, max_value=len(df), step=1, value=10)

        if st.button("Count Values"):
            result = df[column].value_counts().reset_index().head(num_values)
            result.columns = [column, 'Count']
            st.dataframe(result)

            st.subheader("Visualizations")

            # Bar Chart
            fig_bar = px.bar(result, x=column, y='Count', text='Count', template='plotly_white')
            st.plotly_chart(fig_bar)

            # Line Chart
            fig_line = px.line(result, x=column, y='Count', text='Count', template='plotly_white')
            st.plotly_chart(fig_line)

            # Pie Chart
            fig_pie = px.pie(result, names=column, values='Count')
            st.plotly_chart(fig_pie)