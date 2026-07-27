import random

# Demo Market Database

MARKET_DATABASE = {

    "Paddy": {
        "market": "Mysuru APMC",
        "price": 3050
    },

    "Maize": {
        "market": "Mandya APMC",
        "price": 2450
    },

    "Wheat": {
        "market": "Hubballi APMC",
        "price": 2820
    },

    "Cotton": {
        "market": "Raichur APMC",
        "price": 7420
    },

    "Sugarcane": {
        "market": "Belagavi APMC",
        "price": 355
    },

    "Tomato": {
        "market": "Kolar APMC",
        "price": 1850
    },

    "Potato": {
        "market": "Bengaluru APMC",
        "price": 2100
    },

    "Banana": {
        "market": "Mysuru APMC",
        "price": 2400
    }

}


def get_market_price(crop):
    """
    Returns market information.

    Example

    {
        "market":"Mysuru APMC",
        "crop":"Paddy",
        "price":3025
    }
    """

    if crop not in MARKET_DATABASE:

        return {

            "market": "Unknown",

            "crop": crop,

            "price": "--"

        }

    info = MARKET_DATABASE[crop]

    # Simulate daily fluctuation

    price = info["price"] + random.randint(-100, 100)

    return {

        "market": info["market"],

        "crop": crop,

        "price": price

    }
