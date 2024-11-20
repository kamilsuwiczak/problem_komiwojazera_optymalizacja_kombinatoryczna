import time
import matplotlib.pyplot as plt

# funcion returning distance between two points
def distance(p1,p2):
    return ((p1[2]-p2[2])**2 + (p1[1]-p2[1])**2)**0.5

def import_data(pathfile):
    # reading points from file
    with open(pathfile, "r") as file:
        file.readline()
        point_coordinates = file.readlines()
        return point_coordinates
    file.close()

def main():
    point_coordinates = import_data("data/test.txt")

    #converting points to list and to int
    for i in range(len(point_coordinates)):
        point_coordinates[i] = point_coordinates[i].rstrip()
        point_coordinates[i] = point_coordinates[i].split(" ")
        point_coordinates[i][0] = int(point_coordinates[i][0])
        point_coordinates[i][1] = int(point_coordinates[i][1])
        point_coordinates[i][2] = int(point_coordinates[i][2])

    # start measuring time of execution
    start_time = time.time()


    path = "1 -> "
    length = 0
    current_point = point_coordinates[0]
    start_point = current_point
    point_coordinates.pop(0)

    # arrays for plot
    x = [current_point[1]]
    y = [current_point[2]]

    # main core of the program
    for i in range(len(point_coordinates)):
        min_distance = distance(current_point,point_coordinates[0])
        next_point = point_coordinates[0]
        for j in range(1,len(point_coordinates)):
            if distance(current_point,point_coordinates[j]) < min_distance:
                min_distance = distance(current_point,point_coordinates[j])
                next_point = point_coordinates[j]

        x.append(next_point[1])
        y.append(next_point[2])

        path += str(next_point[0]) + " -> "
        length += distance(current_point,next_point)
        current_point = next_point
        point_coordinates.remove(current_point)

    length += distance(current_point,start_point)
    path += "1"

    # end of measuring time
    finish_time = time.time() - start_time

    print("Ścieżka: " + path)
    print("Długość ścieżki: " + str(length))
    print("Czas działania programu: " + str(finish_time))

    # adding coming back to starting point to plot 
    x.append(start_point[1])
    y.append(start_point[2]) 

    # making plot 
    plt.plot(x,y, '-o')
    plt.show()

   

if __name__ == "__main__":
    main()
