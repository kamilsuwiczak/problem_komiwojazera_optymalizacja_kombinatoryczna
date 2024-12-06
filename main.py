import time
import matplotlib.pyplot as plt
import aco 


def main():
    filename="berlin52.txt"
    points =aco.import_data("data/data_mmachowiak/"+filename)
    file=open("results/aco_results.txt","a")
    file.write(f"file: {filename}\n")
    file.close()
    for k in range(1,10):
        for i in range(1,21):
            for j in range(1,21):
                file=open("results/aco_results.txt","a")
                for _ in range(3):
                    best_path,best_distance, time = aco.ant_colony_optimization(points, 10, 100, i, j, k/10, 1)
                    file.write(f"alpha: {i}, beta: {j}, evaporation_rate: {k/10},  best_distance: {best_distance}, time: {time}\n")
                file.write("\n")
                file.close()

if __name__ == "__main__":
    main()
