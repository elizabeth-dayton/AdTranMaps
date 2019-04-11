from Coordinate import MyCoordinate
import csv
from Dijkstra import Graph

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
                coordinate = MyCoordinate(x, y, 'room', name, None)
                self.list_of_coordinates.append(coordinate)
            for i in range(len(self.list_of_coordinates)):
                print(self.list_of_coordinates[i].ID)

    def read_hallway_data(self):
        with open(self.hallway_data, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == "X":
                    continue
                ID = row[0]
                x = row[1]
                y = row[2]
                edges = row[3:]
                for i in range(len(edges)):
                    edges[i] = edges[i].lstrip(' ')
                coordinate = MyCoordinate(x, y, 'hallway', ID, edges)

                '''graph = Graph([])
                for edge in edges:
                    graph.add_edge(ID, edge)
                    print("ID: " + ID + " edge: " + edge)'''

                temp_list = []
                for edge in edges:
                    temp_list.append(f'({ID}, {edge}, 1)')
                    #print("ID: " + ID + " edge: " + edge)
                    print(temp_list)

                self.list_of_coordinates.append(coordinate)

                #graph = Graph(temp_list)

                #print(graph.dijkstra('Hallway1', 'Hallway15'))
            '''for item in self.list_of_coordinates:
                print(item)'''
            #print(self.list_of_coordinates[0].ID)
            #print(graph.dijkstra(self.list_of_coordinates[0].get_ID(), self.list_of_coordinates[5].get_ID()))


test = FloorMap(r'C:\Users\Blake - PC\Desktop\RoomData.csv', r'C:\Users\Blake - PC\Desktop\HallwayData.csv', [])
#test.read_room_data()
test.read_hallway_data()