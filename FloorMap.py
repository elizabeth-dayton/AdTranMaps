from Coordinate import MyCoordinate
import csv

class FloorMap:

    def __init__(self, room_data, hallway_data, list_of_coordinates):
        self.room_data = room_data
        self.hallway_data = hallway_data
        self.list_of_coordinates = list_of_coordinates

    def read_room_data(self):

        with open('RoomData.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row.split(',')[0]
                if name == "Room #":
                    continue
                x = row.split(',')[1]
                y = row.split(',')[2]
                coordinate = MyCoordinate(x, y, 'room', name)
                self.list_of_coordinates.append(coordinate)
                print(name)
                print(x)
                print(y)


