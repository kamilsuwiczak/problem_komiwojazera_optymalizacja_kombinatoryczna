
#reading points from file
pathfile1 = "map_points.txt"
with open(pathfile1, "r") as file1:
    file1.readline()
    point_coordinates = file1.readlines()


#converting points to list and to int
for i in range(len(point_coordinates)):
    point_coordinates[i] = point_coordinates[i].rstrip()
    point_coordinates[i] = point_coordinates[i].split(" ")
    point_coordinates[i].pop(0)
    point_coordinates[i][0] = int(point_coordinates[i][0])
    point_coordinates[i][1] = int(point_coordinates[i][1])

print(point_coordinates)

file1.close()