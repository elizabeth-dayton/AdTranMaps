
class MyCoordinate:

    def __init__(self, x, y, type, ID, edges):
        self.x = x
        self.y = y
        self.type = type
        self.ID = ID
        self.edges = edges

    def is_valid_type(self):
        if self.type is "hallway" or "room":
                return True
        else:
            return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_type(self):
        return self.type

    def get_ID(self):
        return self.ID

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def set_type(self, new_type):
        if is_valid_type(self):
            self.type = new_type
        else:
            print("ERROR 001 - Invalid coordinate type at " + self.x + " " + self.y)

    def __str__(self):
        return "X value is " + self.get_x()
