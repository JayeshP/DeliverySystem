from models import Location, Order, DE

orders = [
    # {
    #     'restaurant_loc': "lat1, long1",
    #     "order_time": "2017-10-10 10:10:10"
    # }
]

des = [
    # {
    #     "id": 123,
    #     "current_loc": "lat2, long2",
    #     "last_order_delivery_time": "2017-10-10 10:15:10",
    # }
]

# hash function to map location to 1 km area
de_mapping_ = [
    {   
        "area_code": [
            "de1", "de2"
        ]
    }
]

a11 = Location(1, 2)
a12 = Location(1, 4)
a13 = Location(1, 5)
a21 = Location(2, 4)
a22 = Location(2, 4)
a31 = Location(3, 7)
a32 = Location(3, 5)

orders.append(Order(a11, '2017-07-29 10:10:10'))
orders.append(Order(a12, '2017-07-29 10:15:10'))
orders.append(Order(a13, '2017-07-29 10:12:10'))
orders.append(Order(a21, '2017-07-29 10:15:10'))
orders.append(Order(a22, '2017-07-29 10:17:10'))
orders.append(Order(a31, '2017-07-29 10:17:10'))
orders.append(Order(a32, '2017-07-29 10:15:10'))

des.append(DE(1, a11, '2017-07-29 09:45:00'))
des.append(DE(2, a11, '2017-07-29 09:50:00'))

des.append(DE(3, a13, '2017-07-29 09:45:00'))
des.append(DE(4, a32, '2017-07-29 09:50:00'))
