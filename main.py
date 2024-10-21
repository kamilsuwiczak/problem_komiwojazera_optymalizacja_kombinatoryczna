

pathfile1 = "map_points.txt"
with open(pathfile1, "r") as file1:
    data = file1.readlines()

points = [[] for i in range(len(data))]
print(points)
#for i in range(len(data)):

for i in range(len(data)):
    data[i] = data[i].split()
print(data)
file1.close()