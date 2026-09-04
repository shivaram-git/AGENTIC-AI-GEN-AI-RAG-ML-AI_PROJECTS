

# 1. import streamlit

import streamlit as st

# 2.  Add a title of your app

st.title("My first Streamlit APP created by Shivaram")

# 3. Add Some Text

st.write("Welcome ! This App calculates the square of a number.")

# 4. Create Interactive slider
st.header('Select a Number')
number = st.slider('Pick a number',0,0,5)

# 5. Calculate and display the result
st.subheader('Result')
squrd_num = number*number
st.write(f'The square of **{number}** is **{squrd_num}**.')
