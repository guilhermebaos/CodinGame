import sys
import math

# Game Constants
SCREEN_WIDTH = 16000
SCREEN_HEIGHT = 9000
CHECKPOINT_RADIUS = 600

# My Parameters
go_to_checkpoint_dist = CHECKPOINT_RADIUS * 1.5
time_for_boost = 4

# Variables
max_dist = 0
boosted = 0

# Distance from next objective at which we'll start slowing down
slowdown_dist = CHECKPOINT_RADIUS * 1.0


# Helper Functions

# Distance from the center of the screen
def dist_from_center(x, y):
    global SCREEN_WIDTH, SCREEN_HEIGHT

    return ((x - SCREEN_WIDTH / 2) ** 2 + (y - SCREEN_HEIGHT / 2) ** 2) ** 0.5


# Angle made between a point and the pod
def angle_to_pod(x, y, point_x, point_y):
    return math.atan((point_y - y) / (point_x - x))


# Targets the point in the checkpoint that will lead to a sherper turn
sharp_turning = [False, False]  # If I'm doing a sharp turn with a [positive, negative] angle


def sharp_turn_target(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_angle, boost_angle):
    global CHECKPOINT_RADIUS, sharp_turning

    checkpoint_angle = angle_to_pod(x, y, next_checkpoint_x, next_checkpoint_y)

    # Calculate the points in the checkpoint perpendicular to the line that connects the pod to the checkpoint
    perpendicular = math.pi / 2 - checkpoint_angle

    target_x1 = next_checkpoint_x + math.cos(perpendicular) * CHECKPOINT_RADIUS
    target_y1 = next_checkpoint_y - math.sin(perpendicular) * CHECKPOINT_RADIUS

    angle1 = checkpoint_angle - angle_to_pod(x, y, target_x1, target_y1)

    target_x2 = next_checkpoint_x - math.cos(perpendicular) * CHECKPOINT_RADIUS
    target_y2 = next_checkpoint_y + math.sin(perpendicular) * CHECKPOINT_RADIUS

    angle2 = checkpoint_angle - angle_to_pod(x, y, target_x2, target_y2)

    # Start a sharp turn
    if next_checkpoint_angle > boost_angle:
        sharp_turning = [True, False]
    elif next_checkpoint_angle < -boost_angle:
        sharp_turning = [False, True]

    # Execute a sharp turn
    print(sharp_turning, file=sys.stderr)
    if sharp_turning[0]:
        if next_checkpoint_angle < -boost_angle:
            sharp_turning[0] = False

        return [int(target_x1), int(target_y1)] if angle1 < 0 else [int(target_x2), int(target_y2)]
    elif sharp_turning[1]:
        if next_checkpoint_angle > boost_angle:
            sharp_turning[1] = False

        return [int(target_x1), int(target_y1)] if angle1 > 0 else [int(target_x2), int(target_y2)]
    else:
        return [int(next_checkpoint_x), int(next_checkpoint_y)]


# Game Loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [float(i) for i in
                                                                                               input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # print(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_angle, file=sys.stderr)

    # Allowed angle to the checkpoint in within wich we can boost.
    # It corresponds to the angle we must have if we're already pointing at the checkpoint
    boost_angle = math.degrees(abs(math.atan(CHECKPOINT_RADIUS / next_checkpoint_dist)))

    # If we're very close to or already pointing at the checkpoint, we just go to it, otherwise we do a sharp turn
    if next_checkpoint_dist <= go_to_checkpoint_dist:
        target_x = int(next_checkpoint_x)
        target_y = int(next_checkpoint_y)
    else:
        target_x, target_y = sharp_turn_target(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_angle,
                                               boost_angle)

    # Formula for thrust
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    else:
        thrust = 100

    # Slowdown if we are very close to the checkpoint
    if next_checkpoint_dist < slowdown_dist:
        thrust *= 1 / next_checkpoint_dist

    thrust = int(thrust)

    # Try to use the BOOST when distance from checkpoint is maximum
    if next_checkpoint_dist >= max_dist:
        max_dist = next_checkpoint_dist * 0.93

        if boosted is True and abs(next_checkpoint_angle) < boost_angle:
            thrust = 'BOOST'
            boosted = False
        elif boosted == time_for_boost:
            boosted = True
        elif boosted < time_for_boost and boosted is not False and boosted is not True:
            boosted += 1

    print(f'{target_x} {target_y} {thrust}')
