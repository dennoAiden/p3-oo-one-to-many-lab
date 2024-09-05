class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # This will use the pet_type property setter
        self.owner = owner  # This will use the owner property setter
        Pet.all.append(self)

    # Getter for pet_type
    @property
    def pet_type(self):
        return self._pet_type

    # Setter for pet_type
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception(f"{value} is not a valid pet type. Choose from {', '.join(Pet.PET_TYPES)}.")
        self._pet_type = value

    # Getter for owner
    @property
    def owner(self):
        return self._owner

    # Setter for owner
    @owner.setter
    def owner(self, value):
        if value is not None and not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        self._owner = value



class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
