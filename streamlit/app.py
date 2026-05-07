import streamlit as st
import pandas as pd
import numpy as np

#title of page
st.title("My First Streamlit App")

#display simple text
st.write("Hello, Streamlit!")

#create a simple datfram
df=pd.DataFrame(
    {
        "first column":[1,2,3,4],
        "second column":[5,6,7,8]
    }
)

#display dataframe
st.write("Here is the data frame")
st.write(df)

#bar chart
st.bar_chart(df)

#create a line chart

chart_data=pd.DataFrame(
    
        np.random.randn(20,3),columns=['a','b','c']
    
)
st.line_chart(chart_data)

st.title("Streamlit text input")
 
name=st.text_input("Enter your name")

if name:
    st.write(f"Hello {name}")

#slider
age = st.slider("Select Age", 0, 100)
st.write(f"Your age is {age}")


#button
if st.button("Click Me"):
    st.write("Button clicked!")

#select box
option = st.selectbox("Choose course", ["DS", "AI", "Web"])
st.write("You slected",option)


#uploading file
df.to_csv("sampledata.csv") #sample csv file for use 

uploaded_file=st.file_uploader("Choose a csv file",type='csv')

if uploaded_file is not None :
    df=pd.read_csv(uploaded_file)
    st.write(df)



