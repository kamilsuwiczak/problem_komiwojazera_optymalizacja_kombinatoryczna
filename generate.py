import random

# function that generates random points (everyone is different than other one)
def generate_data(instance_size, filepath):
    generated_data=[]
    
    # instance_size_multipilcated allows to set how far the points will be
    instance_size_multipilcated = int(instance_size*2.5)
    
    # openig the file
    file = open(filepath, "w")

    for i in range(instance_size):
        generated_point = []
        generated_point.append(random.randint(1,instance_size_multipilcated))
        generated_point.append(random.randint(1,instance_size_multipilcated))

# checking if points are the same and changing it
        while generated_point in generated_data:
            # print("znaleziono powtorke")
            generated_point.clear()
            generated_point.append(random.randint(1,instance_size_multipilcated))
            generated_point.append(random.randint(1,instance_size_multipilcated))

        generated_data.append(generated_point)
        # print(str(i) + " x: " + str(generated_data[i][0]) + " y: " + str(generated_data[i][1]))
    
    # writing to file
    file.write(str(len(generated_data))+"\n")
    for i in range(len(generated_data)):
        file.write(str(i+1)+" " + str(generated_data[i][0]) + " " + str(generated_data[i][1]) + "\n")

    # closing the file
    file.close()
    # print(generated_data)



def main():
    for i in range(1,11):
        generate_data(i*100,f'''data/dane_{i*100}.txt''')


if __name__ == "__main__":
    main()
