import time
import matplotlib.pyplot as plt
import aco
import aco_improved as aco2 


def main():
    for i in range(1,11):
        path = f"data/dane_{i*25}.txt"
        points = aco.import_data(path)
        best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 7, 70, 1.0, 2.0, 0.5, 1.0)
        print(i*25)
        print(best_distance)
    # files = ["berlin52.txt", "bier127.txt", "tsp250.txt", "tsp500.txt", "tsp1000.txt"]
    # for file in files:
    #     points =aco.import_data("data/data_mmachowiak/"+file)
    #     if file == "berlin52.txt":
    #         #best_path,best_distance, time = aco.ant_colony_optimization(points, 40, 600, 1.5, 6, 0.1, 0.005)
    #         # berlin52.txt: (points, 30, 250, 1.5, 6, 0.01, 0.005)
    #         # bier127.txt:  (points, 20, 135, 1.5, 6, 0.01, 0.005)
    #         # tsp250.txt:   (points, 10, 50, 1.5, 6, 0.01, 0.005)
    #         # tsp500.txt:   (points, 5, 15, 1.5, 6, 0.01, 0.005)
    #         # tsp500.txt:   (points, 2, 6, 1.5, 6, 0.01, 0.005)
    #         best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 10, 100, 1.0, 2.0, 0.5, 1.0)
    #     elif file == "bier127.txt":
    #         best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 20, 135, 1.5, 6, 0.01, 0.005)
    #     elif file == "tsp250.txt":
    #         best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 10, 50, 1.5, 6, 0.01, 0.005)
    #     elif file == "tsp500.txt":
    #         best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 5, 15, 1.5, 6, 0.01, 0.005)
    #     elif file == "tsp1000.txt":
    #         best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 2, 5, 1.5, 6, 0.01, 0.005)
    #     #print("Best Path:", best_path)
    #     print("Best Distance:", best_distance)
    #     print("Time:", elapsed_time)

if __name__ == "__main__":
    main()
