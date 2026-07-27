import streamlit as st
from PIL import Image
from datetime import date

# Import project modules
from utils.crop_detector import detect_crop
from utils.disease_detector import detect_disease
from utils.stage_detector import detect_stage
from utils.weather import get_weather
from utils.market import get_market_price

st.set_page_config(
    page_title="AgriVision AI",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 AgriVision AI")
st.subheader("AI Powered Smart Agriculture Platform")

st.sidebar.header("Farm Information")

location = st.sidebar.text_input(
    "Location",
    value="Mysuru"
)

sowing_date = st.sidebar.date_input(
    "Sowing Date",
    value=date.today()
)

land_area = st.sidebar.number_input(
    "Land Area (Acres)",
    min_value=0.5,
    max_value=100.0,
    value=1.0
)

uploaded_image = st.file_uploader(
    "📷 Upload Crop Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:

    image = Image.open(uploaded_image)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🤖 Analyze Crop"):

        with st.spinner("Running AI Models..."):

            crop = detect_crop(image)

            disease = detect_disease(image)

            stage = detect_stage(image)

            weather = get_weather(location)

            market = get_market_price(crop["crop"])

        st.success("Analysis Completed")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🌾 Crop Analysis")

            st.metric(
                "Crop",
                crop["crop"]
            )

            st.metric(
                "Confidence",
                f'{crop["confidence"]}%'
            )

            st.metric(
                "Growth Stage",
                stage["stage"]
            )

            st.metric(
                "Disease",
                disease["disease"]
            )

        with col2:

            st.subheader("📈 Prediction")

            st.metric(
                "Health",
                f'{disease["health"]}%'
            )

            st.metric(
                "Estimated Yield",
                f'{int(land_area*22)} Quintals'
            )

            st.metric(
                "Harvest",
                stage["harvest"]
            )

        st.divider()

        st.subheader("🌦 Weather")

        st.write(
            f"Temperature : {weather['temperature']} °C"
        )

        st.write(
            f"Humidity : {weather['humidity']} %"
        )

        st.write(
            f"Condition : {weather['condition']}"
        )

        st.divider()

        st.subheader("💰 Market Price")

        st.write(
            f"Market : {market['market']}"
        )

        st.write(
            f"Crop : {market['crop']}"
        )

        st.write(
            f"Price : ₹{market['price']} / Quintal"
        )

        st.divider()

        st.subheader("💡 AI Recommendation")

        if disease["disease"] == "Healthy":

            st.success(
                "Crop is healthy. Continue irrigation and nutrient management."
            )

        else:

            st.warning(
                f"Detected {disease['disease']}. Spray the recommended fungicide and monitor the crop."
            )
