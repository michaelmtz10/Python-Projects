class building:
     def __init__(self, material_type, paint_color, type, cost):
         self.material_type = material_type
         self.paint_color = paint_color
         self.type = type
         self.cost = cost
# created a building class to be the parent of different types of buildings

house = building("wood", "brown/white", "residential", 58000)

class tower(building):
    def __init__(self, floor_count, parking_lot_size):
        self.floor_count = floor_count
        self.parking_lot_size = parking_lot_size

# created the tower class with the parent class building and added properties

class apartment(building):
    def __init__(self, room_count, personal_garage, rent):
        self.room_count = room_count
        self.personal_garage = personal_garage
        self.rent = rent
apt1 = apartment(34, 18, 2000)
print(apt1.room_count)