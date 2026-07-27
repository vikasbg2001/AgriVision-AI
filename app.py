import streamlit as st
from PIL import Image
from datetime import date

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgriVision AI")
st.subheader("AI Crop Growth & Harvest Prediction (Prototype)")

uploaded_file = st.file_uploader(
    "Upload Crop Image",
    type=["jpg", "jpeg", "png"]
)

sowing_date = st.date_input(
    "Sowing Date",
    value=date.today()
)

location = st.text_input(
    "Farm Location"
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Crop",
        use_container_width=True
    )

    if st.button("Analyze Crop"):

        st.success("Analysis Complete")

        st.write("### AI Result")

        st.metric("Crop", "Paddy")

        st.metric("Health", "92%")

        st.metric("Growth Stage", "Flowering")

        st.metric("Harvest", "18 Days Remaining")

        st.metric("Estimated Yield", "40 Quintals")

        st.metric("Ready to Harvest", "No")
