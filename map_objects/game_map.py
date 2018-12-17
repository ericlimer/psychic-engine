from random import randint

from map_objects.tile import Tile
from map_objects.rectangle import Rect

class GameMap:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        return tiles 

    def make_map(self, max_rooms, room_min_size, room_max_size, map_width, map_height, player):
        
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            w = randint(room_min_size, room_max_size)
            h = randint(room_min_size, room_max_size)

            x = randint(0, map_width - w - 1)
            y = randint(0, map_height - h - 1)

            new_room = Rect(x, y, w, h)
            print("new room {} {} {} {}" .format(x, y, w, h))

            for other_room in rooms:
                if new_room.intersect(other_room):
                    print("interset")
                    break
            else:
                    #new room doesnt intersect and so is valid
                self.create_room(new_room)
                print("create room")

                (new_x, new_y) = new_room.center()

                if num_rooms == 0:
                 # if this is the first room
                    player.x = new_x
                    player.y = new_y
                    print("place player coords")
            rooms.append(new_room)
            num_rooms += 1
        

    def create_room(self, room):
        for x in range(room.x1+1, room.x2):
            for y in range(room.y1+1, room.y2):
                    self.tiles[x][y].blocked = False
                    self.tiles[x][y].blocks_sight = False
        self.create_door(room)

    def create_door(self, room):
        if randint(0,1):
            
            door_x = randint(room.x1+1,room.x2-1)
            door_y = room.y1

            self.tiles[door_x][door_y].blocked = False
            self.tiles[door_x][door_y].blocks_sight = False

            
        if randint(0,1):

            door_x = room.x1
            door_y = randint(room.y1+1, room.y2-1)

            self.tiles[door_x][door_y].blocked = False
            self.tiles[door_x][door_y].blocks_sight = False


        if randint(0,1):

            door_x = randint(room.x1+1,room.x2-1)
            door_y = room.y2

            self.tiles[door_x][door_y].blocked = False
            self.tiles[door_x][door_y].blocks_sight = False

        if randint(0,1):

            door_x = room.x2
            door_y = randint(room.y1+1, room.y2-1)

            self.tiles[door_x][door_y].blocked = False
            self.tiles[door_x][door_y].blocks_sight = False
    

    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].blocks_sight = False
    
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2) +1):
            self.tiles[x][y].blocked = False
            self.tiles[x][y].blocks_sight = False
    

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True
        return False
