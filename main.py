from sportPackages import SportPackage
import json

from const import URLS, DUMP
from utils import create_dict_from_list, fetch_json


data1 = fetch_json(URLS[0])
data2 = fetch_json(URLS[1])
data3 = fetch_json(URLS[2])

dict_package_1 = create_dict_from_list(
    data1
    if isinstance(data1, list)
    else data1.get("response", {}).get("matching_all", {}).get("docs", [])
)
dict_package_2 = create_dict_from_list(data2.get("items", []) if data2 else [])
dict_package_3 = create_dict_from_list(
    data3.get("response", {}).get("matching_all", {}).get("docs", []) if data3 else []
)
if DUMP:
    json.dump(dict_package_1, open("PZU.json", "w",encoding="utf-8"), indent=4)
    json.dump(dict_package_2, open("Medicover.json", "w",encoding="utf-8"), indent=4)
    json.dump(dict_package_3, open("Multisport.json", "w",encoding="utf-8"), indent=4)

package_1 = SportPackage(name="PZU Sport Package", objects=dict_package_1)
package_2 = SportPackage(name="OK System Package", objects=dict_package_2)
package_3 = SportPackage(name="Benefit Systems Package", objects=dict_package_3)

search_term = "CityFit Targówek"

exists_in_package_1 = package_1.facility_exists(search_term)
exists_in_package_2 = package_2.facility_exists(search_term)
exists_in_package_3 = package_3.facility_exists(search_term)

print(f"Search term '{search_term}' exists in PZU Sport Package: {exists_in_package_1}")
print(f"Search term '{search_term}' exists in OK System Package: {exists_in_package_2}")
print(
    f"Search term '{search_term}' exists in Benefit Systems Package: {exists_in_package_3}"
)

if exists_in_package_1 and exists_in_package_2 and exists_in_package_3:
    print(f"The facility '{search_term}' exists in all sport packages.")
else:
    print(f"The facility '{search_term}' does not exist in all sport packages.")
