import streamlit as st

st.title("OpenCV Streamlit Test")
st.header("header")

image = st.file_uploader("Upload an image file", type=['jpg', 'jpeg', 'png'])
# display image
# st.image(image)

st.text("This is text")


selection = st.selectbox("Select Box", ["None", "F1", "F2"])
st.write(selection)
checkbox_val = st.checkbox("Apply Filter")
st.write(checkbox_val)
