import sys

# PARAMETERS
FEAR_RADIUS = 5  # Distance at which the bot starts to run away


def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# See what moves are best in order to try to go to a specific place
def move_in_direction(dx, dy):
    # Determine the order of importance of the moves
    move_order = []
    if abs(dx) > abs(dy):
        if dx > 0:
            move_order += ['RIGHT']
            least_important = 'LEFT'
        else:
            move_order += ['LEFT']
            least_important = 'RIGHT'

        if dy > 0:
            move_order += ['UP', 'DOWN']
        else:
            move_order += ['DOWN', 'UP']

    else:
        if dy > 0:
            move_order += ['UP']
            least_important = 'DOWN'
        else:
            move_order += ['DOWN']
            least_important = 'UP'

        if dx > 0:
            move_order += ['RIGHT', 'LEFT']
        else:
            move_order += ['LEFT', 'RIGHT']

    move_order += [least_important]
    return move_order


# Run away from an enemy. We know the enemy's relative position to us
def run_away(dx, dy):
    # Determine the order of importance of the moves
    move_order = []
    if abs(dx) < abs(dy):
        if dx > 0:
            move_order += ['LEFT']
            least_important = 'RIGHT'
        else:
            move_order += ['RIGHT']
            least_important = 'LEFT'

        if dy > 0:
            move_order += ['DOWN', 'UP']
        else:
            move_order += ['UP', 'DOWN']

    else:
        if dy > 0:
            move_order += ['DOWN']
            least_important = 'UP'
        else:
            move_order += ['UP']
            least_important = 'DOWN'

        if dx > 0:
            move_order += ['LEFT', 'RIGHT']
        else:
            move_order += ['RIGHT', 'LEFT']

    move_order += [least_important]
    return move_order


# Board Size
board_size = [int(input()), int(input())]

# Number of characters
char_num = int(input())

board = [['?' for _ in range(board_size[1] + 1)] for _ in range(board_size[0] + 1)]

# Game Loop
last_move = None
been_there = []
objectives = []
while True:
    move_order = []
    fear = False

    # The orthogonal directions! -> Tells us if there is a wall next to us.
    # fov = [DOWN, RIGHT, UP, LEFT] -> Discovered by trying to move against walls
    fov = [input() for _ in range(4)]
    print(fov, '\n', file=sys.stderr)

    # Coordinates of the enemies
    coords = [[] for _ in range(char_num)]
    for index in range(char_num):
        # Get the coordinates
        coords[index] = [int(j) for j in input().split()]
        board[coords[index][1]][coords[index][0]] = '_'
        print(coords[index], file=sys.stderr)

    # My coordinates
    my_coords = coords.pop()
    mx, my = my_coords
    if my_coords not in been_there:
        been_there += [my_coords]
        if my_coords in objectives:
            objectives.remove(my_coords)

    # Update the board with our acquired knowledge
    for index, space in enumerate(fov):
        if index == 0:
            space_coords = [mx, my - 1]
        elif index == 1:
            space_coords = [mx + 1, my]
        elif index == 2:
            space_coords = [mx, my + 1]
        elif index == 3:
            space_coords = [mx - 1, my]
        board[space_coords[1]][space_coords[0]] = space

        if space == '_' and space_coords not in been_there and space_coords not in objectives:
            objectives.insert(0, space_coords)

    # My objective is explore
    my_obj = objectives[0]
    ox, oy = my_obj
    # print('\n\n', my_obj, file=sys.stderr)

    # Allows us to see the board
    for line in board:
        print(''.join(line), file=sys.stderr)

    # Run away from enemies
    for enemy in coords:
        d = man_dist(my_coords, enemy)
        if d <= FEAR_RADIUS:
            print('FEAR!', file=sys.stderr)
            fear = True
            ex, ey = enemy

            dx = ex - mx
            dy = ey - my
            move_order += move_in_direction(dx, dy)[::-1]

    # Possible movements, discovered by observing what coordinate changes
    # Each move has an associated letter and number. The number corresponds to the fov index for that direction
    moves = {
        'UP': ['D', 2],
        'RIGHT': ['A', 1],
        'DOWN': ['C', 0],
        'LEFT': ['E', 3],
        'WAIT': 'B'
    }

    # Try to get closer to the objective
    dx = ox - mx
    dy = oy - my

    move_order += move_in_direction(dx, dy)

    # Prevent opposites moves
    opposite_moves = [['RIGHT', 'LEFT'], ['LEFT', 'RIGHT'], ['UP', 'DOWN'], ['DOWN', 'UP']]

    for m in move_order:
        if ([m, last_move] in opposite_moves) and (not fear):
            move_order += [m]
            last_move = None
        elif fov[moves[m][1]] == '_':
            print(moves[m][0])
            last_move = m
            break
