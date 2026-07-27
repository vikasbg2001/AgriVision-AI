# AgriVision-AI
# 🌾 AgriVision AI

An AI-powered Smart Agriculture platform built using Streamlit and YOLOv8.

---

# Features

✅ Crop Identification

✅ Disease Detection

✅ Growth Stage Detection

✅ Harvest Prediction

✅ Yield Prediction

✅ Weather Forecast

✅ Market Prices

---

# Project Structure

```
AgriVision-AI/

│

├── app.py

├── config.py

├── requirements.txt

│

├── models/

│ ├── crop_model.pt

│ ├── disease_model.pt

│ └── stage_model.pt

│

├── utils/

│ ├── crop_detector.py

│ ├── disease_detector.py

│ ├── stage_detector.py

│ ├── weather.py

│ └── market.py

│

├── uploads/

└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AgriVision-AI.git

cd AgriVision-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# AI Models

Place your trained YOLO models here

```
models/

crop_model.pt

disease_model.pt

stage_model.pt
```

---

# Weather API

Create an OpenWeather account

https://openweathermap.org/api

Generate an API Key

Replace

```
YOUR_OPENWEATHER_API_KEY
```

inside

```
config.py
```

or set

```
OPENWEATHER_API_KEY
```

as an environment variable.

---

# Future Features

- GPS
- Firebase Login
- Marketplace
- Soil Analysis
- Satellite Images
- Fertilizer Recommendation
- Pest Prediction
- Mobile App

---

# Author

Developed using

- Python
- Streamlit
- YOLOv8
- PyTorch
- OpenCV
