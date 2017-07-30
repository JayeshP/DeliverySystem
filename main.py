
from test import orders
from order_preprocessor import order_area_map
from de_preprocessor import de_map, des

nearest_areas = {
    1: [1, 2, 3],
    2: [2, 1, 3],
    3: [3, 2, 3]
}

print("\n\nMain............................................\n\n")

# processing orders interval of 5 mins
for order in orders:
    order_area_code = order.restaurant_loc.get_area_code()

    # print('order_area_code', order_area_code)

    if not nearest_areas.get(order_area_code):
        order_nearest_area = [order_area_code]
    else:
        order_nearest_area = nearest_areas[order_area_code]

    # picking area based on first mile
    for area in order_nearest_area:
        if not de_map.get(area):
            # print('no DE in given area...')
            continue

        nearer_des = de_map[area].pop()
        print "assigning DE to Order"
        print('Order - ', order.restaurant_loc.lat, order.restaurant_loc.long, order.order_time)

        print('DE - ', nearer_des.id, nearer_des.current_loc.lat, nearer_des.current_loc.long, nearer_des.last_order_delivery_time)
        continue

    print('No one available - ', order.restaurant_loc.lat, order.restaurant_loc.long, order.order_time)
