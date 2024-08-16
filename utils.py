import requests
import difflib


def create_dict_from_list(list_of_dicts):
    new_dict = {}
    for item in list_of_dicts:
        try:
            # Check if the item has 'basicParameters' and use the first key for the name
            if "basicParameters" in item and isinstance(item["basicParameters"], dict):
                key = item["basicParameters"].get(
                    "1"
                )  # '1' seems to represent the facility name
            else:
                key = item.get("title") or item.get("name")

            if key:  # Ensure the key is not None
                new_dict[key] = item
        except Exception as e:
            print(f"Got a problem with {item}: {e}")
    return new_dict


def search_dict(dictionary, search_term, cutoff=0.6):
    if not search_term:
        print("Search term is None or empty.")
        return []

    matches = difflib.get_close_matches(
        search_term, dictionary.keys(), n=5, cutoff=cutoff
    )
    return [
        (match, difflib.SequenceMatcher(None, search_term, match).ratio())
        for match in matches
    ]


def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}, Status Code: {response.status_code}")
        return None


def make_hashable(item):
    """Recursively make an item hashable."""
    if isinstance(item, dict):
        return tuple((k, make_hashable(v)) for k, v in item.items())
    elif isinstance(item, list):
        return tuple(make_hashable(i) for i in item)
    elif isinstance(item, set):
        return tuple(sorted(make_hashable(i) for i in item))
    else:
        return item
import math

def haversine(lat1, lon1, lat2, lon2, R=6371.0):
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
