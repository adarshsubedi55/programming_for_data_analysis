import streamlit as st
import pandas as pd
import plotly.express as px
import io

#Load your own cleaned data:
df = pd.read_csv("hypertension_dataset_5000.csv")
#Add your title and purpose statement:
st.title("app.py")

st.info(
    "Write a short statement explaining the purpose of your app "
    "and that it is not a diagnostic tool."
)

rows_to_show = st.selectbox(
    "Number of rows to display",
    [5, 10, 20, 50, 100]
)

st.dataframe(
    df.head(rows_to_show),
    use_container_width=True
)

col1, col2 = st.columns(2)

col1.metric("Number of Rows", df.shape[0])
col2.metric("Number of Columns", df.shape[1])

st.write(df.columns.tolist())

categorical_variables = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

numerical_variables = df.select_dtypes(
    include="number"
).columns.tolist()


st.expander("View Dataset Information")

buffer = io.StringIO()
df.info(buf=buffer)

info_text = buffer.getvalue()
st.text(info_text)

st.subheader("Statistical Summary")

st.dataframe(
    df.describe().T,
    use_container_width=True
)

#Use st.metric() and st.columns() to summarise the population.
col1, col2, col3, col4 = st.columns(4)

col1.metric("Sleep_Hours", 8)
col2.metric("Gender", ...)
col3.metric("BMI", ...)
col4.metric("Physical_Activity", ...)



