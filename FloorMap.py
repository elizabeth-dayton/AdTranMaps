from Coordinate import MyCoordinate
import csv

class FloorMap:

    def __init__(self, room_data, hallway_data, list_of_coordinates):
        self.room_data = room_data
        self.hallway_data = hallway_data
        self.list_of_coordinates = list_of_coordinates

    def read_room_data(self):

        with open(self.room_data, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                if name == "Room #":
                    continue
                x = row[1]
                y = row[2]
                coordinate = MyCoordinate(x, y, 'room', name)
                self.list_of_coordinates.append(coordinate)
            for i in range(len(self.list_of_coordinates)):
                print(self.list_of_coordinates[i].ID)

    def read_hallway_data(self):

        with open(self.hallway_data, newline='') as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if row[0] == "X":
                    continue
                x = row[0]
                y = row[1]
                coordinate = MyCoordinate(x, y, 'hallway', 'Hallway' + str(count))
                self.list_of_coordinates.append(coordinate)
                count += 1
            for i in range(len(self.list_of_coordinates)):
                print(self.list_of_coordinates[i].x)


test = FloorMap(r'C:\Users\Blake - PC\Desktop\RoomData.csv', r'C:\Users\Blake - PC\Desktop\HallwayData.csv', [])
#test.read_room_data()
test.read_hallway_data()