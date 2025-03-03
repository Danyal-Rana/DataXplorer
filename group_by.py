import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    st.title("Group By Analysis")
    st.subheader("Summarize Data by Specific Categories")

    # Check if data is uploaded
    if 'data' not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state['data']

    with st.expander("Group By Your Columns"):
        col1, col2, col3 = st.columns(3)

        with col1:
            groupby_cols = st.multiselect("Select Columns to Group By", options=df.columns)

        with col2:
            operation_col = st.selectbox("Select Column to Perform Operation", options=df.columns)

        with col3:
            operation = st.selectbox("Select Operation", options=["mean", "sum", "count", "min", "max"])

        if groupby_cols:
            result = df.groupby(groupby_cols).agg({operation_col: operation}).reset_index()
            result.columns = groupby_cols + [f"{operation} of {operation_col}"]
            st.dataframe(result)

            st.subheader("Data Visualization")

            graph_type = st.selectbox("Select Graph", options=['Line', 'Bar', 'Scatter', 'Pie', 'Sunburst'])

            if graph_type == 'Line':
                x_axis = st.selectbox("Select X-axis", options=result.columns)
                y_axis = st.selectbox("Select Y-axis", options=result.columns)
                color = st.selectbox("Select Color", options=[None] + list(result.columns))
                fig = px.line(result, x=x_axis, y=y_axis, color=color, markers=True)
                st.plotly_chart(fig)

            elif graph_type == 'Bar':
                x_axis = st.selectbox("Choose X axis", options=result.columns)
                y_axis = st.selectbox("Choose Y axis", options=result.columns)
                color = st.selectbox("Color Information", options=[None] + list(result.columns))
                facet_col = st.selectbox("Column Information", options=[None] + list(result.columns))
                fig = px.bar(result, x=x_axis, y=y_axis, color=color, facet_col=facet_col, barmode='group')
                st.plotly_chart(fig)

            elif graph_type == 'Scatter':
                x_axis = st.selectbox("Choose X axis", options=result.columns)
                y_axis = st.selectbox("Choose Y axis", options=result.columns)
                color = st.selectbox("Color Information", options=[None] + list(result.columns))
                size = st.selectbox("Size Column", options=[None] + list(result.columns))
                fig = px.scatter(result, x=x_axis, y=y_axis, color=color, size=size)
                st.plotly_chart(fig)

            elif graph_type == 'Pie':
                values = st.selectbox("Choose Numerical Values", options=result.columns)
                names = st.selectbox("Choose Labels", options=result.columns)
                fig = px.pie(result, values=values, names=names)
                st.plotly_chart(fig)

            elif graph_type == 'Sunburst':
                path = st.multiselect("Choose Hierarchical Path", options=result.columns)
                if path:
                    fig = px.sunburst(result, path=path, values=f"{operation} of {operation_col}")
                    st.plotly_chart(fig)