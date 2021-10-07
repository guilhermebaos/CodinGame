import sys
import math

# This solution first displays the cars as following:

# Each value is the order of arrival
# Each index the cars' index in a list sorted by weight


# In such a list, to the right of a value are the heavier cars and to the left are the lighter cars
# As such, we can just make the longest sequence of increasing position for the lighter cars (they'll both be lighter and come later)
# And repeat for the heavier cars!



# See the maximum growing sequence inside an array
# Max growing weight of cars in a train
def max_growing_len(cars, train, train_len):
    global max_len

    if train_len > max_len:
        max_len = train_len

    # Cars that can still be added to the train
    cars = [c for c in cars[:] if c > train[-1]]
    cars_len = len(cars)

    # Stop exploring a path if it won't lead to a new max length
    if cars_len == 0 or train_len + cars_len <= max_len:
        return


    # Select the car
    next_car = cars.pop(0)

    # Try putting the car in the train
    if train_len == 0 or next_car > train[-1]:
        max_growing_len(cars[:], train[:] + [next_car], train_len + 1)

    # Try skipping this car
    max_growing_len(cars[:], train[:], train_len)
    return


# Get the cars in order
n = int(input())
cars = [int(i) for i in input().split()]

# Sort the cars
sorted_cars = cars[:]
sorted_cars.sort()

# See how many cars are lighter/ heavier than each car
cars_sorted_index = [cars.index(i) for i in sorted_cars]

# Try to build a train starting at each car
result = 0
max_len = 0
for start in range(n):
    start_max_len = 0

    # Get the order of the cars that are lighter (left)/ heavier (right) than the starting car
    index = cars_sorted_index.index(start)

    left = cars_sorted_index[:index]
    right = cars_sorted_index[index + 1:]
    left.reverse()

    max_growing_len(left, [start], 1)
    start_max_len += max_len
    max_len = 0

    max_growing_len(right, [start], 1)
    start_max_len += max_len - 1
    max_len = 0

    if start_max_len > result:
        result = start_max_len

    if n - start <= result:
        break

print(result)
