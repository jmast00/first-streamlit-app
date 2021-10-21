import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#Q1
st.title('Week 4 Homework')

#Q2
st.markdown('Name: [Jennifer Mast](https://github.com/jmast00)')
st.write('ID: 60161778')

#Q3
fileupload = st.file_uploader('upload a file',type = ['csv'])

#Q4 Q5
if fileupload is not None:
    df = pd.read_csv(fileupload)
    df = df.applymap(lambda x: np.nan if x == ' ' else x)   
else:
    st.write('please upload a file')
    st.write('here is a sample DataFrame')
    df = pd.DataFrame(
        np.array(
            [[1, 9, 3, 6, 8], [4, 5, 12, 6, 13], [2, 3, 7, 8, 9]]
            ),columns=['a', 'b', 'c','d','e']
        )
    

#Q6
def can_numeric(c):
    try:
        pd.to_numeric(df[c])
        return True
    except:
        return False

#Q7
good_cols = [c for c in df.columns if can_numeric(c)]
df[good_cols] = df[good_cols].apply(pd.to_numeric, axis = 0)
df_good_cols = df[good_cols]
st.write(df_good_cols)

#Q8
x_axis = st.selectbox('choose an x value', good_cols)
y_axis = st.selectbox('choose a y value', good_cols)

#Q9
s = st.slider('how many rows?', 0, len(df.index)-1)

#Q10
x = df.iloc[s]
m1 = np.mean(df.loc[:,x_axis])
m2 = np.mean(df.loc[:,y_axis])
st.write(f'Average {x_axis} is {m1} ')
st.write(f'Average {y_axis} is {m2} ')
st.write(f'you picked {s} rows to graph')

#Q11 
st.altair_chart(alt.Chart(df_good_cols[:s]).mark_circle().encode(
    x=x_axis,
    y=y_axis,
    tooltip = (x_axis, y_axis),
))
     

#Q12
but = st.button("Click me!")
if but == True:
    st.write("nice!")
          

