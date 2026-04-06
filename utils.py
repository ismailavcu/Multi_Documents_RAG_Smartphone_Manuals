import re

PHONE_MODELS = [
    "note20",
    "z fold7",
    "s23 fe",
    "s26 ultra"
]


def normalize(text: str):
    """
    Lowercase + remove all non-alphanumeric characters
    Example:
    'S 23-FE' -> 's23fe'
    'zfold 7' -> 'z fold7'
    's26ultra' -> 's26 ultra'
    's 26 ultra' -> 's26 ultra'
    etc.
    """
    return re.sub(r'[^a-z0-9]', '', text.lower())


def extract_phone_model(query: str):
    normalized_query = normalize(query)

    for model in PHONE_MODELS:
        normalized_model = normalize(model)

        if normalized_model in normalized_query:
            return model

    return None


#print(extract_phone_model("asdas s26ultra asda")) # for test