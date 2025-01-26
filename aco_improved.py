import numpy as np
import matplotlib.pyplot as plt
import time

def import_data(filepath):
    with open(filepath, "r") as file:
        file.readline()
        point_coordinates = file.readlines()
        for i in range(len(point_coordinates)):
            point_coordinates[i] = point_coordinates[i].rstrip()
            point_coordinates[i] = point_coordinates[i].split(" ")
            point_coordinates[i][0] = int(point_coordinates[i][0])
            point_coordinates[i][1] = int(point_coordinates[i][1])
            point_coordinates[i][2] = int(point_coordinates[i][2])
        return point_coordinates

def distance(p1, p2):
    return np.sqrt((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def generate_distance_matrix(points):
    n = len(points)
    distance_matrix = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = distance(points[i], points[j])
    return distance_matrix

def two_opt(path, distance_matrix):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1: continue
                if distance_matrix[path[i - 1]][path[i]] + distance_matrix[path[j - 1]][path[j]] > \
                   distance_matrix[path[i - 1]][path[j - 1]] + distance_matrix[path[i]][path[j]]:
                    path[i:j] = path[j - 1:i - 1:-1]
                    improved = True
    return path

def ant_colony_optimization(points, num_ants, num_iterations, alpha, beta, evaporation_rate, pheromone_init):
    start_time = time.time()
    n_points = len(points)
    distance_matrix = generate_distance_matrix(points)

    pheromones = np.ones([n_points, n_points]) * pheromone_init
    best_distance = float('inf')
    best_path = None

    initial_beta = beta

    for iter_num in range(num_iterations):
        all_paths = []
        all_distances = []

        for ant in range(num_ants):
            path = []
            visited = []
            current = 0
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

            path.append(path[0])
            distance = sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
            path = two_opt(path, distance_matrix) 
            distance = sum(distance_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
            all_paths.append(path)
            all_distances.append(distance)

        for i, distance in enumerate(all_distances):
            if distance < best_distance:
                best_distance = distance
                best_path = all_paths[i]

        pheromones *= (1 - evaporation_rate)
        for i, path in enumerate(all_paths):
            for j in range(len(path) - 1):
                pheromones[path[j]][path[j + 1]] += 1 / all_distances[i]

        best_path_contribution = 1 / best_distance
        for i in range(len(best_path) - 1):
            pheromones[best_path[i]][best_path[i + 1]] += best_path_contribution

        beta = initial_beta * (1 - iter_num / num_iterations)

    for i in range(len(best_path)):
        best_path[i] += 1

    return best_path, best_distance, time.time() - start_time

def aco_visualisation(best_path, points):
    x = []
    y = []
    for i in best_path:
        x.append(points[i - 1][1])
        y.append(points[i - 1][2])

    plt.plot(x, y, '-o')
    plt.title("ACO Optimized Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
