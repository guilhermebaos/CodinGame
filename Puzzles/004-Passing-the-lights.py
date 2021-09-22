def convert_to_int_vel(num):
    return int(num * 3.6)


# Case Parameters
max_speed_road = int(input()) / 3.6  # Convert to meters per second
light_count = int(input())


# Finds the possible speeds the car can have to reach a traffic light while it's green
def find_possible_speeds(dist, time):
    global max_speed_road

    # Number of times the light has switched colors
    n = 0
    while True:
        # Time interval we can pass in
        max_time = time * (n + 1)
        min_time = time * n

        max_speed = dist / min_time if min_time != 0 else max_speed_road
        min_speed = dist / max_time

        n += 2
        if min_speed > max_speed_road:
            continue

        yield [min_speed, min(max_speed, max_speed_road)]


# Get a generator for each light that gives the minimum and maximum velocities
gen_min_max_vel = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    gen_min_max_vel += [find_possible_speeds(distance, duration)]

# Current interval values for every traffic light
vel_intervals = {
    'min': [],
    'max': []
}
for gen in gen_min_max_vel:
    mini, maxi = next(gen)
    vel_intervals['min'] += [mini]
    vel_intervals['max'] += [maxi]

# Search for a velocity that passes all lights on green
while True:
    maximum_min = max(vel_intervals['min'])
    minimum_max = min(vel_intervals['max'])

    # If there is a value for which all intervals align, that's our solution!
    # We have to convert to km/h because only integer speeds are allowed
    if convert_to_int_vel(maximum_min) < convert_to_int_vel(minimum_max):
        # Convert back to km/h
        print(convert_to_int_vel(minimum_max))
        break

    # Lower the minimum
    index = vel_intervals['min'].index(maximum_min)
    mini, maxi = next(gen_min_max_vel[index])
    vel_intervals['min'][index] = mini
    vel_intervals['max'][index] = maxi
