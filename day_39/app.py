# import libraries
import streamlit as st
from PIL import Image

# set page title
st.set_page_config(page_title="Image Classification", page_icon=":guardsman:", layout="wide")

# page header
st.header("Image Classification")

# page subheader
st.subheader("Upload an image to classify")

# upload image
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# display image
if image is not None:
    img = Image.open(image)
    st.image(img)
    st.success("Image uploaded successfully!")


# upload video
video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

# display video
if video is not None:
    st.video(video)
    st.success("Video uploaded successfully!")

# upload audio
audio = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

# display audio
if audio is not None:
    st.audio(audio)
    st.success("Audio uploaded successfully!")

# upload document
document = st.file_uploader("Upload a document", type=["pdf", "docx"])

# display document
if document is not None:
    st.download_button("Download document", document, "document.pdf", "application/pdf")
    st.success("Document uploaded successfully!")

