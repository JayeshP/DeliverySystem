import math
# Delivery Executive
class DE:
    def __init__(self, id_, current_loc, last_order_delivery_time):
        self.id = id_
        self.current_loc = current_loc
        self.last_order_delivery_time = last_order_delivery_time


class Order:
    def __init__(self, restaurant_loc, order_time):
        self.restaurant_loc = restaurant_loc
        self.order_time = order_time

class Location:
    def __init__(self, lat, long_):
        self.lat = lat
        self.long = long_

    @classmethod
    def distance_bet_two_point(cls, lat, long_):
        return math.sqrt(math.pow(self.lat-lat, 2) + math.pow(self.long - long_, 2))

    # 1 km block area
    def get_area_code(self):
        # hash function to convert loc to area code
        # sample data
        if self.lat == 1:
            return 1
        if self.lat == 2:
            return 2
        if self.lat == 3:
            return 3

        return 1

    def get_nearest_areas():
        # sample data
        return [1, 2, 3]
