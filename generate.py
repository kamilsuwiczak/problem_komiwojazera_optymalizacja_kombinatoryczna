import random
import os
import sys

def generate_data(instance_size):
    generated_data=[]
    instance_size_multipilcated = int(instance_size*0.7)
    for i in range(instance_size):
        generated_point = []
        generated_point.append(random.randint(1,instance_size_multipilcated))
        generated_point.append(random.randint(1,instance_size_multipilcated))
        while generated_point in generated_data:
            print("znaleziono powtorke")
            generated_point.clear()
            generated_point.append(random.randint(1,instance_size_multipilcated))
            generated_point.append(random.randint(1,instance_size_multipilcated))
        generated_data.append(generated_point)
        
        print(str(i) + " x: " + str(generated_data[i][0]) + " y: " + str(generated_data[i][1]))    




    print(generated_data)


generate_data(3)



