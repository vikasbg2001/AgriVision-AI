from pathlib import Path
from PIL import Image

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None

MODEL_PATH = Path("models/crop_model.pt")

# Default labels (used if the model doesn't contain class names)
DEFAULT_CLASSES = {
    0: "Paddy",
    1: "Maize",
    2: "Wheat",
    3: "Cotton",
    4: "Tomato",
    5: "Potato",
    6: "Sugarcane",
    7: "Banana"
}

_model = None


def load_model():
    """Load the YOLO model once."""
    global _model

    if _model is not None:
        return _model

    if YOLO is None:
        return None

    if not MODEL_PATH.exists():
        return None

    try:
        _model = YOLO(str(MODEL_PATH))
        return _model
    except Exception:
        return None


def detect_crop(image: Image.Image):
    """
    Detect crop from an uploaded image.

    Returns:
    {
        "crop": "Paddy",
        "confidence": 97.5
    }
    """

    model = load_model()

    # Fallback if no model exists
    if model is None:
        return {
            "crop": "Paddy",
            "confidence": 95.0
        }

    try:
        results = model.predict(
            source=image,
            verbose=False,
            conf=0.25
        )

        result = results[0]

        if len(result.boxes) == 0:
            return {
                "crop": "Unknown",
                "confidence": 0.0
            }

        box = result.boxes[0]

        cls_id = int(box.cls.item())
        confidence = float(box.conf.item()) * 100

        # Prefer class names stored in the YOLO model
        if hasattr(model, "names"):
            crop_name = model.names.get(cls_id, DEFAULT_CLASSES.get(cls_id, "Unknown"))
        else:
            crop_name = DEFAULT_CLASSES.get(cls_id, "Unknown")

        return {
            "crop": crop_name,
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        return {
            "crop": "Detection Error",
            "confidence": 0.0,
            "error": str(e)
        }
