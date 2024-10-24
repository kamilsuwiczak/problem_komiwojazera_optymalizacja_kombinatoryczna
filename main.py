import time
def distance(p1,p2):
    return ((p1[2]-p2[2])**2 + (p1[1]-p2[1])**2)**0.5

#reading points from file
pathfile1 = "test.txt"
with open(pathfile1, "r") as file1:
    #file1.readline()
    point_coordinates = file1.readlines()
file1.close()

point_coordinates[0]=[0,0,0]

#converting points to list and to int
for i in range(1,len(point_coordinates)):
    point_coordinates[i] = point_coordinates[i].rstrip()
    point_coordinates[i] = point_coordinates[i].split(" ")
    point_coordinates[i][0] = int(point_coordinates[i][0])
    point_coordinates[i][1] = int(point_coordinates[i][1])
    point_coordinates[i][2] = int(point_coordinates[i][2])

# print(point_coordinates)

# measuring time of execution
start_time = time.time()

path = "0 -> "
length = 0
current_point = point_coordinates[0]
point_coordinates.pop(0)

for i in range(len(point_coordinates)):
    min_distance = distance(current_point,point_coordinates[0])
    next_point = point_coordinates[0]
    for j in range(1,len(point_coordinates)):
        if distance(current_point,point_coordinates[j]) < min_distance:
            min_distance = distance(current_point,point_coordinates[j])
            next_point = point_coordinates[j]
    path += str(next_point[0]) + " -> "
    length += distance(current_point,next_point)
    current_point = next_point
    point_coordinates.remove(current_point)

length += distance(current_point,[0,0,0])

path += "0"

finish_time = time.time() - start_time

print("Ścieżka: " + path)
print("Długość ścieżki: " + str(length))
print("Czas działania programu: " + str(finish_time))

