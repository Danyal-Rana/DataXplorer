import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def show():
    st.title("Data Visualizations")
    st.subheader("Explore Your Data with Different Charts")

    # Check if data is uploaded
    if 'data' not in st.session_state:
        st.warning("Please upload a dataset first.")
        return

    df = st.session_state['data']

    st.sidebar.header("Visualization Options")
    plot_type = st.sidebar.selectbox("Select Plot Type", 
                                     ["Histogram", "Box Plot", "Scatter Plot", 
                                      "Line Chart", "Bar Chart", "Correlation Heatmap"])

    st.subheader(f"{plot_type}")

    if plot_type == "Histogram":
        column = st.selectbox("Select Column for Histogram", df.columns)
        bins = st.slider("Number of Bins", min_value=5, max_value=50, value=20)
        
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=bins, kde=True, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Box Plot":
        column = st.selectbox("Select Column for Box Plot", df.columns)
        
        fig, ax = plt.subplots()
        sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)

    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        color = st.selectbox("Color By", [None] + list(df.columns))
        
        fig = px.scatter(df, x=x_col, y=y_col, color=color)
        st.plotly_chart(fig)

    elif plot_type == "Line Chart":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        
        fig, ax = plt.subplots()
        sns.lineplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)

    elif plot_type == "Bar Chart":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        color = st.selectbox("Color By", [None] + list(df.columns))
        
        fig = px.bar(df, x=x_col, y=y_col, color=color, barmode="group")
        st.plotly_chart(fig)

    elif plot_type == "Correlation Heatmap":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        st.pyplot(fig)