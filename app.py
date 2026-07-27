import streamlit as st
from PIL import Image
from datetime import date, datetime

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgriVision AI")
st.write("AI Crop Growth & Harvest Prediction Prototype")

uploaded_file = st.file_uploader(
    "Upload Crop Image",
    type=["jpg", "jpeg", "png"]
)

col1, col2 = st.columns(2)

with col1:
    sowing_date = st.date_input(
        "Sowing Date",
        value=date.today()
    )

with col2:
    location = st.text_input(
        "Farm Location",
        placeholder="Example: Mysuru"
    )

area = st.number_input(
    "Land Area (Acres)",
    min_value=0.5,
    max_value=100.0,
    value=1.0
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Crop",
        use_container_width=True
    )

    if st.button("Analyze Crop"):

        today = datetime.today().date()

        days = (today - sowing_date).days

        if days < 30:
            stage = "Seedling"
            harvest = 90
        elif days < 70:
            stage = "Vegetative"
            harvest = 50
        elif days < 100:
            stage = "Flowering"
            harvest = 20
        else:
            stage = "Mature"
            harvest = 0

        st.success("Analysis Completed")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Crop", "Paddy")
            st.metric("Health", "92%")
            st.metric("Growth Stage", stage)
            st.metric("Disease", "Healthy")

        with c2:
            st.metric("Harvest Remaining", f"{harvest} Days")
            st.metric("Estimated Yield", f"{int(area*20)} Quintals")
            st.metric("Market Price", "₹2950 / Quintal")
            st.metric("Location", location)

        st.subheader("Recommendation")

        if harvest == 0:
            st.success("Crop is Ready for Harvest")
        else:
            st.info(f"Estimated harvest after {harvest} days.")

        st.warning("Weather API will be connected in the next version.")
