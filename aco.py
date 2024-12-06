import numpy as np
import matplotlib.pyplot as plt
import time

def import_data(filepath):
    with open(filepath, "r") as file:
        file.readline()
        point_coordinates = file.readlines()
        #converting points to list and to int
        for i in range(len(point_coordinates)):
            point_coordinates[i] = point_coordinates[i].rstrip()
            point_coordinates[i] = point_coordinates[i].split(" ")
            point_coordinates[i][0] = int(point_coordinates[i][0])
            point_coordinates[i][1] = int(point_coordinates[i][1])
            point_coordinates[i][2] = int(point_coordinates[i][2])
        return point_coordinates
    file.close()

# funcion returning distance between two points
def distance(p1, p2):
    return np.sqrt((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

# matrix of distances between points
def generate_distance_matrix(points):
    n = len(points)
    distance_matrix = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = distance(points[i], points[j])
    return distance_matrix

# Ant Colony Optimization
def ant_colony_optimization(points, num_ants, num_iterations, alpha, beta, evaporation_rate, pheromone_init):
    start_time = time.time()
    n_points = len(points)
    distance_matrix = generate_distance_matrix(points)
    
    pheromones = np.ones([n_points, n_points]) * pheromone_init
    best_distance = float('inf')
    best_path = None
    
    for _ in range(num_iterations):
        all_paths = []
        all_distances = []
        
        for i in range(num_ants):
            path = []
            visited = list()
            current = 0
            # current = np.random.randint(n_points)
            path.append(current)
            visited.append(current)
            
            while len(path) < n_points:
                probabilities = []
                for i in range(n_points):
                    if i not in visited:
                        tau = pheromones[current][i] ** alpha
                        eta = (1 / distance_matrix[current][i]) ** beta
                        probabilities.append(tau * eta)
                    else:
                        probabilities.append(0)
                
                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()
                next_node = np.random.choice(range(n_points), p=probabilities)
                path.append(next_node)
                visited.append(next_node)
                current = next_node
                if (time.time()- start_time )> 180:
                    return best_path, best_distance
            path.append(path[0])
            distance = sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
            all_paths.append(path)
            all_distances.append(distance)
        
        # update best path
        for i, distance in enumerate(all_distances):
            if distance < best_distance:
                best_distance = distance
                best_path = all_paths[i]
        
        # update pheromones
        pheromones *= (1 - evaporation_rate)
        for i, path in enumerate(all_paths):
            for j in range(len(path) - 1):
                pheromones[path[j]][path[j + 1]] += 1 / all_distances[i]
    
    for i in range(len(best_path)):
        best_path[i] = best_path[i] + 1
        
    return best_path, best_distance

# plotting the best path
def aco_visualisation(best_path, points):
    x=[]
    y=[]
    for i in best_path:
        x.append(points[i-1][1])
        y.append(points[i-1][2])
    
    plt.plot(x, y, '-o')
    plt.title("ACO")
    plt.show()

def main():
    start_time = time.time()
    points = import_data("data/data_mmachowiak/bier127.txt")
    
    results =[]
    for _ in range(1):
        best_path, best_distance = ant_colony_optimization(points, num_ants=10, num_iterations=100, alpha=1, beta=15, evaporation_rate=0.1, pheromone_init=1)
        results.append([best_path, best_distance])
    results.sort(key=lambda x: x[1])

    finish_time = time.time() - start_time 

    print("Najlepsza trasa:", results[0][0])
    print("Najkrótsza odległość:", results[0][1])
    print("Czas działania programu:", finish_time)
    for i in range(len(results)):
        print(results[i][1])

    aco_visualisation(results[0][0], points)

if __name__ == "__main__":  
    main()