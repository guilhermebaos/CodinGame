# Number of temperatures
n = int(input())


def print_closest_to_0():
    # If there are no temperatures, return 0
    if n == 0:
        print('0')
        return

    # Get and organize the temperatures
    temps = []
    abs_temp = []
    for i in input().split():
        t = int(i)
        temps += [t]
        abs_temp += [abs(t)]

    # Get the minimum absolute temperature
    closest_temp = min(abs_temp)

    # All temperatures that have an absolute value equal to the minimum are possible results
    possible_results = []
    for t in temps:
        if abs(t) == closest_temp:
            possible_results += [t]

    # Return a positive result if there is one, otherwise return a negative number
    print(max(possible_results))


print_closest_to_0()
