import streamlit as st
st.title("STREAMLIT CLASS")
st.header("PRACTISE CLASS")
st.subheader("CLASS TWO")
st.success("SUCCESSFUL")

from PIL import Image

img = Image.open("c:\\Users\\DELL\\Pictures\\Inked_DSC0587_LI.jpg")
st.image(img,width=300)

st.checkbox("Blue")
st.checkbox("Black")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):

	st.success("Male")
else:
	st.success("Female")
	
hobby = st.multiselect("Hobbies: ",['Dancing', 'Reading', 'Sports'])

# Create a text area with a placeholder

long_description = st.text_area(
    label="Enter a long description:", 
	
# The label for the input field
    placeholder="Write your detailed description here..."
)

# Display the entered input
if long_description:
    st.write("Your description:")
    st.write(long_description)
	
level = st.slider("Select the level", 1, 10)
	
st.text('Selected: {}'.format(level))
	
