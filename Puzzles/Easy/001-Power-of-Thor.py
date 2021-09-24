light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Amount to move in each direction
    delta_x = light_x - initial_tx
    delta_y = light_y - initial_ty

    # Select the next move
    if light_x > initial_tx:
        if light_y > initial_ty:
            move = [1, 1, 'SE']
        elif light_y == initial_ty:
            move = [1, 0, 'E']
        else:
            move = [1, -1, 'NE']
    elif light_x == initial_tx:
        if light_y > initial_ty:
            move = [0, 1, 'S']
        else:
            move = [0, -1, 'N']
    else:
        if light_y > initial_ty:
            move = [-1, 1, 'SW']
        elif light_y == initial_ty:
            move = [-1, 0, 'W']
        else:
            move = [-1, -1, 'NW']

    # The new initial positions are the positions after the next move
    initial_tx += move[0]
    initial_ty += move[1]

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(move[2])