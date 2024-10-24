# CREATING MULTIPAGES
import streamlit as st
st.set_page_config(
    page_title="AINA PYTHON DAY4"
    )

st.markdown('# This is the main page...')
st.sidebar.write('main page')

import streamlit as st


st.warning("FIRST PART")

st.success("1) TRY")
# TRY
st.write("Hello Guys! How are you today?")
st.write("How do I stop this session?")
st.write("I am Nur Aina Najihah")
st.write("HAI HAI")
st.write("hahahahahahahaha")

# TEXT FORMATTING
st.success("2) TEXT FORMATTING")
st.write("Hello friends")
st.header("Hello friends")
st.subheader("Hello friends")
st.caption("Hello friends")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')
st.markdown("Here's a bouquet &mdash;\ :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

# ADVANCED FONT
st.success("3) ADVANCED FONT")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)


########    UI COMPONENT    ########
st.warning("UI COMPONENT")

# SELECTION BOX
st.success("1) SELECTION BOX")

st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])

st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

# BUTTONS
st.success("2) BUTTON")

st.button("Click Here to Proceed")

st.slider("Select the length of stay", 1,10, value=3)

# INPUT BOX
st.success("3) INPUT BOX")

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")

st.write("The current number is ", number)

# INSERT GRAPHICS
st.success("4) INSERT GRAPHICS")
from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

# DATAFRAME
st.success("5) DATAFRAME")
import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

# BAR CHART
st.success("6) BAR CHART")
st.bar_chart(df, x="Location", y="Income")

# LINE CHART
st.success("7) LINE CHART")
st.line_chart(df, x="Household", y="Income")

# SCATTER CHART
st.success("8) SCATTER CHART")
st.scatter_chart(df, x="Household", y="Income")

# CREATING MULTI - TAB PAGE
st.success("9) CREATING MULTI - TAB PAGE")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header ("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header ("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header ("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


# CREATING MULTI - COLUMNS
st.success("9) CREATING MULTI - COLUMNS")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# CREATING MULTI - COLUMNS FOR GRAPH
st.success("9) CREATING MULTI - COLUMNS FOR GRAPH")

col1, col2 = st.columns(2)
with col1:
    st.header("BAR CHART")
    st.bar_chart(df, x="Location", y="Income")
with col2:
    st.header("SCATTER CHART")
    st.scatter_chart(df, x="Household", y="Income")

