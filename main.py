
def distance(p1,p2):
    return ((p1[2]-p2[2])**2 + (p1[1]-p2[1])**2)**0.5

#reading points from file
pathfile1 = "map_points.txt"
with open(pathfile1, "r") as file1:
    #file1.readline()
    point_coordinates = file1.readlines()
point_coordinates[0]=[0,0,0]

#converting points to list and to int
for i in range(1,len(point_coordinates)):
    point_coordinates[i] = point_coordinates[i].rstrip()
    point_coordinates[i] = point_coordinates[i].split(" ")
    point_coordinates[i][0] = int(point_coordinates[i][0])
    point_coordinates[i][1] = int(point_coordinates[i][1])
    point_coordinates[i][2] = int(point_coordinates[i][2])

print(point_coordinates)
path = "0 -> "
length = 0
current_point = point_coordinates[0]
point_coordinates.pop(0)

for i in range(len(point_coordinates)):
    min_distance = 1000000
    for point in point_coordinates:
        if distance(current_point,point) < min_distance:
            min_distance = distance(current_point,point)
            next_point = point
    path += str(next_point[0]) + " -> "
    length += distance(current_point,next_point)
    current_point = next_point
    point_coordinates.remove(current_point)
path += "0"
length += distance(current_point,[0,0,0])
print(path,length)
file1.close()