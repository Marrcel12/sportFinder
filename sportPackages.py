from utils import search_dict


class SportPackage:
    def __init__(self, name, objects, name_of_owner="Twoja Stara"):
        self.name = name
        self.objects = objects
        self.name_of_owner = name_of_owner

    def facility_exists(self, name):
        return bool(search_dict(self.objects, name))