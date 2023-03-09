CONSUMPTION = 12 # km / l

spent_time = int(input()) # h
average_speed = int(input()) # km / h

distance_travelled = average_speed * spent_time
spent_fuel = distance_travelled / CONSUMPTION

print(f'{spent_fuel:.3f}')
