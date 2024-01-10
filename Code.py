class TransmissionTower:
    def __init__(self, code_name, height, material, capacity):
        valid_ids = ["Squirrel", "Gopher", "Weasel", "Ferret", "Rabbit"]
        
        if code_name not in valid_ids:
            raise ValueError(f"code_name must be one of the following: {', '.join(valid_ids)}")
        self.code_name = code_name
        self.height = height
        self.material = material
        self.capacity = capacity

    def display_info(self):
        print(f"Transmission Tower {self.code_name} Information:")
        print(f"Height: {self.height} meters")
        print(f"Material: {self.material}")
        print(f"Capacity: {self.capacity} watts")




