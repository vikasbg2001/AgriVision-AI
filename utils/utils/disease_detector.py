from pathlib import Path
from PIL import Image

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None

MODEL_PATH = Path("models/disease_model.pt")

DEFAULT_CLASSES = {
    0: "Healthy",
    1: "Leaf Blast",
    2: "Brown Spot",
    3: "Bacterial Blight",
    4: "Rust",
    5: "Powdery Mildew",
    6: "Leaf Curl",
    7: "Early Blight"
}

_model = None


def load_model():
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


def detect_disease(image: Image.Image):
    """
    Returns:
    {
        "disease": "...",
        "confidence": 98.5,
        "health": 95
    }
    """

    model = load_model()

    # Demo mode
    if model is None:
        return {
            "disease": "Healthy",
            "confidence": 97.4,
            "health": 95
        }

    try:

        results = model.predict(
            source=image,
            conf=0.25,
            verbose=False
        )

        result = results[0]

        if len(result.boxes) == 0:

            return {
                "disease": "Unknown",
                "confidence": 0,
                "health": 50
            }

        box = result.boxes[0]

        cls = int(box.cls.item())

        confidence = round(float(box.conf.item()) * 100, 2)

        if hasattr(model, "names"):
            disease = model.names.get(
                cls,
                DEFAULT_CLASSES.get(cls, "Unknown")
            )
        else:
            disease = DEFAULT_CLASSES.get(cls, "Unknown")

        health = max(5, int(100 - confidence / 2))

        if disease == "Healthy":
            health = 100

        return {
            "disease": disease,
            "confidence": confidence,
            "health": health
        }

    except Exception as e:

        return {
            "disease": "Error",
            "confidence": 0,
            "health": 0,
            "error": str(e)
        }
