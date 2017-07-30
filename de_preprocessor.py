from test import des

de_map = {}

print "\n\nDES...........................................................\n\n"
# This is a worker, Once the order is placed, it comes into this queue
for de in des:
    print(de.id, de.current_loc.lat, de.current_loc.long, de.last_order_delivery_time)
    area_code = de.current_loc.get_area_code()
    if area_code in de_map:
        # Assumption - DE will be free in order of time
        de_map[area_code].append(de)
    else:
        de_map[area_code] = [de]

# just printing area code and its orders
for area_code, des in de_map.iteritems():
    print('area code -', area_code)
    for de in des:
        print(de.id, de.current_loc.lat, de.current_loc.long, de.last_order_delivery_time)
