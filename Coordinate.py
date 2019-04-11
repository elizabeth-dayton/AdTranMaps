class Coordinate:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        if not is_valid_type(self):
            print("ERROR 001 - Invalid coordinate type at " + self.x + " " + self.y)

    def is_valid_type(self):
        if self.type is "hallway" or "door" or "office" or "conference_room" or "lobby" or "bathroom" or \
            "closet" or "stairs" or "elevator" or "medical_room":
                return True
        else:
            return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_type(self):
        return self.type

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def set_type(self, new_type):
        if is_valid_type(self):
            self.type = new_type
        else:
            print("ERROR 001 - Invalid coordinate type at " + self.x + " " + self.y)
