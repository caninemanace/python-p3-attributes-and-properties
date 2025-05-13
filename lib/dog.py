APPROVED_BREEDS = [
    "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
    "French Bulldog", "Pug", "Pointer"
]

class Dog:
    def __init__(self, name="Not provided", breed="Mastiff"):
        self._name = None
        self._breed = None

        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            return  # Prevent breed from being set if name is invalid

        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
