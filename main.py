import time
import matplotlib.pyplot as plt
import aco
import aco_improved as aco2 


def main():
    filename="tsp1000.txt"
    points =aco.import_data("data/data_mmachowiak/"+filename)
    for i in range(10):
        #best_path,best_distance, time = aco.ant_colony_optimization(points, 40, 600, 1.5, 6, 0.1, 0.005)
        # berlin52.txt: (points, 30, 250, 1.5, 6, 0.01, 0.005)
        # bier127.txt:  (points, 20, 135, 1.5, 6, 0.01, 0.005)
        # tsp250.txt:   (points, 10, 50, 1.5, 6, 0.01, 0.005)
        # tsp500.txt:   (points, 5, 15, 1.5, 6, 0.01, 0.005)
        # tsp500.txt:   (points, 2, 6, 1.5, 6, 0.01, 0.005)
        best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 2, 5, 1.5, 6, 0.01, 0.005)
        print("Best Path:", best_path)
        print("Best Distance:", best_distance)
        print("Elapsed Time:", elapsed_time)
        print(f"best_distance: {best_distance}, time: {time}")

if __name__ == "__main__":
    main()
