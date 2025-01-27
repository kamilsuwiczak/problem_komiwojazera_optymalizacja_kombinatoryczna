import time
import matplotlib.pyplot as plt

# Function returning the distance between two points
def distance(p1, p2):
    return ((p1[2] - p2[2])**2 + (p1[1] - p2[1])**2)**0.5

for data_size in range(1, 11):
    # Reading points from file
    pathfile = f"data/dane_{data_size*25}.txt"

    with open(pathfile, "r") as file:
        file.readline()
        point_coordinates = file.readlines()

    # Converting points to list and to int
    for i in range(len(point_coordinates)):
        point_coordinates[i] = point_coordinates[i].rstrip()
        point_coordinates[i] = point_coordinates[i].split(" ")
        point_coordinates[i][0] = int(point_coordinates[i][0])
        point_coordinates[i][1] = int(point_coordinates[i][1])
        point_coordinates[i][2] = int(point_coordinates[i][2])

    # Start measuring execution time
    start_time = time.time()

    # Initialize path variables
    path = f"{point_coordinates[0][0]} -> "
    length = 0
    current_point = point_coordinates[0]
    point_coordinates.pop(0)

    # Arrays for plot
    x = [current_point[1]]
    y = [current_point[2]]

    # Main core of the program
    for i in range(len(point_coordinates)):
        min_distance = distance(current_point, point_coordinates[0])
        next_point = point_coordinates[0]
        for j in range(1, len(point_coordinates)):
            if distance(current_point, point_coordinates[j]) < min_distance:
                min_distance = distance(current_point, point_coordinates[j])
                next_point = point_coordinates[j]

        x.append(next_point[1])
        y.append(next_point[2])

        path += str(next_point[0]) + " -> "
        length += distance(current_point, next_point)
        current_point = next_point
        point_coordinates.remove(current_point)

    # Adding the return to the starting point
    length += distance(current_point, [0, x[0], y[0]])
    path += str(x[0])

    # End of measuring execution time
    finish_time = time.time() - start_time

    print("Wielkość pliku: " + str(data_size*25))
    print("Długość Ścieżki: " + str(length))
    print("Czas działania programu: " + str(finish_time))

# # Adding return to starting point to plot
# x.append(x[0])
# y.append(y[0])

# # Making plot
# plt.plot(x, y, '-o')
# plt.title("Greedy algorithm")
# plt.show()
