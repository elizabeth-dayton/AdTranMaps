from Coordinate import MyCoordinate
import csv
from Dijkstra import Graph
from pprint import pprint
import turtle

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
            edge_list = []
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

                for edge in edges:
                    edge_list.append((ID, edge, 1))

                self.list_of_coordinates.append(coordinate)

        edge_list.pop(0)
        graph = Graph(edge_list)
        #print(edge_list)
        print(graph.dijkstra('2263', '2254'))
        path = graph.dijkstra('2263', '2254')

        coord_list = []
        for i in range(len(path)):
            #print(path[i])
            for item in self.list_of_coordinates:
                if path[i] in item.ID:
                    coord_list.append((item.x.lstrip(' '), item.y.lstrip(' ')))

        pprint(coord_list)
        draw(coord_list)

def draw(coordinates):
    obj = turtle.Turtle()
    turtle.bgpic(r'C:\Users\Blake - PC\Desktop\FLOOR_GIF.gif')
    #window.setworldcoordinates(0,0, 950, 650)
    obj.setx(int(coordinates[0][0]))
    obj.sety(int(coordinates[0][1]))
    window = turtle.Screen()
    for item in coordinates:
        #obj.goto(int(item[0]), int(item[1]))
        obj.setx(int(item[0]))
        obj.sety(int(item[1]))
        print (item[0], item[1])

    turtle.done()


test = FloorMap(r'C:\Users\Blake - PC\Desktop\RoomData.csv', r'C:\Users\Blake - PC\Desktop\HallwayData.csv', [])
#test.read_room_data()
test.read_hallway_data()