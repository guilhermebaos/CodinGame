import sys
import math

# CONSTANTS
g = 3.711  # Gravity
max_angle = math.degrees(math.asin(g / 4))  # Maximum angle for constant vertical velocity at thrust 4

# FIRST INPUTS

# The number of points used to draw the surface of Mars.
surface_n = int(input())
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    surface += [[int(j) for j in input().split()]]


# HELPER FUNCTIONS
def find_flat(surface):
    for index in range(len(surface) - 1):
        if surface[index][1] == surface[index + 1][1]:
            return [surface[index][0], surface[index + 1][0]]


def dist_to_flat(x, flat):
    start, end = flat
    if x < start:
        return start - x
    elif x > end:
        return end - x
    else:
        return 0


# Find the flat surface
flat = find_flat(surface)

# Game Loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    dist = dist_to_flat(x, flat)
    direction = -1 if dist < 0 else 1

    # CONTOL SYSTEM
    new_rotate = 0
    new_power = 3
    min_h_speed = 10  # Minimum acceptable horizontal speed

    # DATA ANALASYS

    # Horizontal Speed Info
    delta_h_speed = abs(min_h_speed - abs(h_speed))  # Delta v we need to get to min_h_speed
    h_acc = math.sin(math.radians(45)) * 4  # Horizontal Acceleration

    time_to_h_decelerate = 1.2 * delta_h_speed / h_acc  # Time to decelerate given by Delta v over a

    delta_h_pos = time_to_h_decelerate * (h_speed + min_h_speed) / 2  # Delta h position if we start breaking now

    final_h_pos = x + delta_h_pos

    # Get to landing area ASAP
    if dist != 0:
        new_rotate = -45 * direction
        new_power = 4

        # HSC -> HORIZONTAL SPEED CONTROL

        # Activate HSC if we are already going to stop in the right area if we start breaking now, Position = x + vt, where v is average speed of the interval!
        if (flat[0] < final_h_pos < flat[1]):
            if abs(h_speed) > min_h_speed:
                new_rotate = 45 * (1 if h_speed > 0 else -1)

        elif (flat[0] < final_h_pos and dist >= 0) or (flat[1] > final_h_pos and dist <= 0):
            new_rotate = 45 * (1 if h_speed > 0 else -1)

        # VSC -> VERTCAL SPEED CONTROL

        # Make sure we keep a constant vertical speed
        if abs(new_rotate) > max_angle:
            if abs(v_speed) > 35:
                new_rotate = -max_angle * direction

    # LP -> LANDING PROTOCOL

    # Start landing protocols
    if dist == 0:
        # Local HSC (Horizontal Speed Control)
        if flat[0] + 100 > final_h_pos:
            new_rotate = -45
            new_power = 4
        elif flat[1] - 100 < final_h_pos:
            new_rotate = 45
            new_power = 4

        if abs(h_speed) > min_h_speed:
            new_rotate = 45 * (1 if h_speed > 0 else -1)
            new_power = 4

        # Local VSC (Vertical Speed Control)
        print(v_speed, file=sys.stderr)
        if v_speed < -35:
            new_power = 4
            new_rotate = 0
        elif v_speed > -15:
            new_power = 3

    # print(rotate power)
    print(f'{int(new_rotate)} {new_power}')
