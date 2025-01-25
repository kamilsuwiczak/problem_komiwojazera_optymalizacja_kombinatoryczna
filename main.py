import time
import matplotlib.pyplot as plt
import aco
import aco_improved as aco2 


def main():
    filename="bier127.txt"
    points =aco.import_data("data/data_mmachowiak/"+filename)
    # file=open("results/aco_results.txt","a")
    # file.write(f"file: {filename}\n")
    # file.close()
    # for k in range(1,10):
    #     for i in range(1,21):
    #         for j in range(1,21):
    #             file=open("results/aco_results.txt","a")
    #             for _ in range(3):
    #                 best_path,best_distance, time = aco.ant_colony_optimization(points, 10, 100, i, j, k/10, 1)
    #                 file.write(f"alpha: {i}, beta: {j}, evaporation_rate: {k/10},  best_distance: {best_distance}, time: {time}\n")
    #             file.write("\n")
    #             file.close()
    ## best parameters alpha 1 beta 14 evaporation_rate 0.1
    for i in range(10):
        #best_path,best_distance, time = aco.ant_colony_optimization(points, 40, 600, 1.5, 6, 0.1, 0.005)
        # berlin52.txt: (points, 30, 250, 1.5, 6, 0.01, 0.005)
        # bier127.txt: (points, 20, 130, 1.5, 6, 0.01, 0.005)
        best_path, best_distance, elapsed_time = aco2.ant_colony_optimization(points, 20, 130, 1.5, 6, 0.01, 0.005)
        print("Best Path:", best_path)
        print("Best Distance:", best_distance)
        print("Elapsed Time:", elapsed_time)
        print(f"best_distance: {best_distance}, time: {time}")

if __name__ == "__main__":
    main()
