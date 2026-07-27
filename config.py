import os

# -------------------------------
# Application Configuration
# -------------------------------

APP_NAME = "AgriVision AI"
VERSION = "1.0.0"

# -------------------------------
# AI Models
# -------------------------------

CROP_MODEL = "models/crop_model.pt"
DISEASE_MODEL = "models/disease_model.pt"
STAGE_MODEL = "models/stage_model.pt"

# -------------------------------
# Weather API
# -------------------------------

OPENWEATHER_API_KEY = os.getenv(
    "OPENWEATHER_API_KEY",
    "YOUR_OPENWEATHER_API_KEY"
)

# -------------------------------
# Upload Settings
# -------------------------------

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png"
]

# -------------------------------
# Default Values
# -------------------------------

DEFAULT_LOCATION = "Mysuru"

DEFAULT_MARKET = "Mysuru APMC"

# -------------------------------
# Supported Crops
# -------------------------------

SUPPORTED_CROPS = [

    "Paddy",

    "Maize",

    "Wheat",

    "Cotton",

    "Sugarcane",

    "Tomato",

    "Potato",

    "Banana"

]
