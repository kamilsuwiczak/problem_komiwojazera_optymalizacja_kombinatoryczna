import numpy as np

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

# Funkcja obliczająca odległość między dwoma punktami
def distance(p1, p2):
    return np.sqrt((p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

# Macierz odległości
def generate_distance_matrix(points):
    n = len(points)
    distance_matrix = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            distance_matrix[i][j] = distance(points[i], points[j])
    return distance_matrix

# Parametry ACO
def ant_colony_optimization(points, num_ants=10, num_iterations=100, alpha=1, beta=2, evaporation_rate=0.5, pheromone_init=1):
    n_points = len(points)
    dist_matrix = generate_distance_matrix(points)
    
    # Początkowy poziom feromonów
    pheromones = np.ones([n_points, n_points]) * pheromone_init
    best_distance = float('inf')
    best_path = None
    
    for _ in range(num_iterations):
        all_paths = []
        all_distances = []
        
        for _ in range(num_ants):
            path = []
            visited = set()
            current = np.random.randint(n_points)
            path.append(current)
            visited.add(current)
            
            while len(path) < n_points:
                probabilities = []
                for i in range(n_points):
                    if i not in visited:
                        tau = pheromones[current][i] ** alpha
                        eta = (1 / dist_matrix[current][i]) ** beta
                        probabilities.append(tau * eta)
                    else:
                        probabilities.append(0)
                
                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()
                next_node = np.random.choice(range(n_points), p=probabilities)
                path.append(next_node)
                visited.add(next_node)
                current = next_node
            
            # Powrót do punktu startowego
            path.append(path[0])
            distance = sum(dist_matrix[path[i]][path[i + 1]] for i in range(len(path) - 1))
            all_paths.append(path)
            all_distances.append(distance)
        
        # Aktualizacja najlepszej ścieżki
        for i, distance in enumerate(all_distances):
            if distance < best_distance:
                best_distance = distance
                best_path = all_paths[i]
        
        # Aktualizacja feromonów
        pheromones *= (1 - evaporation_rate)
        for i, path in enumerate(all_paths):
            for j in range(len(path) - 1):
                pheromones[path[j]][path[j + 1]] += 1 / all_distances[i]
    
    return best_path, best_distance


def main():
    # Dane wejściowe
    points = import_data("data/test.txt")
    

    #]Uruchomienie ACO
    best_path, best_distance = ant_colony_optimization(points)

    # Wynik
    print("Najlepsza trasa:", best_path)
    print("Najkrótsza odległość:", best_distance)

if __name__ == "__main__":  
    main()