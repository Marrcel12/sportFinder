from utils import haversine

# NOT WORKING
def find_closest_common_gym(packages, lat, lon, search_term="Si\u0142ownia"):
    common_gyms = None

    # Find gyms that exist in all packages
    for package in packages:
        gyms_in_package = set()
        for facility_name, facility_details in package.objects.items():
            if search_term in facility_details.get("additionalAttributes", []) or "Fitness" in facility_details.get("additionalAttributes", []):
                gyms_in_package.add(facility_name)

        if common_gyms is None:
            common_gyms = gyms_in_package
        else:
            common_gyms.intersection_update(gyms_in_package)

    if not common_gyms:
        return None

    # Find the closest gym among the common gyms
    closest_gym = None
    min_distance = float('inf')

    for package in packages:
        for facility_name in common_gyms:
            facility_details = package.objects[facility_name]
            facility_lat = float(facility_details["basicParameters"]["2"])
            facility_lon = float(facility_details["basicParameters"]["3"])
            distance = haversine(lat, lon, facility_lat, facility_lon)
            
            if distance < min_distance:
                min_distance = distance
                closest_gym = {
                    "name": facility_name,
                    "distance": distance,
                    "address": facility_details["basicParameters"].get("4", "No address"),
                    "city": facility_details["basicParameters"].get("7", "Unknown city"),
                    "url": facility_details["basicParameters"].get("17", "No URL")
                }

    return closest_gym


