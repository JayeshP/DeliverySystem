from test import orders

print "\n\norders...........................................................\n\n"
order_area_map = {}

# This is a worker, Once the order is placed, it comes into this queue
for order in orders:
    # append orders to area code
    print(order.restaurant_loc.lat, order.restaurant_loc.long, order.order_time)
    area_code = order.restaurant_loc.get_area_code()
    if area_code in order_area_map:
        # assumption - since order will come in order of time
        order_area_map[area_code].append(order)
    else:
        order_area_map[area_code] = [order]


# just printing area code and its orders
for area_code, orders in order_area_map.iteritems():
    print('area code -', area_code)
    for order in orders:
        print(order.restaurant_loc.lat, order.restaurant_loc.long, order.order_time)
