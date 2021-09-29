import sys
import math

# Game Constants
CHECKPOINT_RADIUS = 600

# My Parameters
boost_angle = 10  # Allowed angle to the checkpoint in within wich we can boost

# Variables
max_dist = 0
boosted = 0
time_for_boost = 3

# Distance from next objective at which we'll start slowing down
slowdown_dist = CHECKPOINT_RADIUS * 1.0

# Game Loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in
                                                                                               input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    target_x = next_checkpoint_x
    target_y = next_checkpoint_y

    # Formula for thrust
    if abs(next_checkpoint_angle) > 90:
        thrust = 0
    else:
        thrust = 100

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
        elif boosted is not False and boosted < 3:
            boosted += 1

    print(f'{target_x} {target_y} {thrust}')
