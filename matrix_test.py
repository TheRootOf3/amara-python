'''file for testing matrices generation times'''

import time
import matplotlib.pyplot as plt
from matrix_generator import *

def test(number_of_cycles, number_of_iterations):
    for i in range (1, number_of_cycles+1):

        time_lst=[]
        y_lst=[]
        ones_perc_list=[]


        for j in range(1,number_of_iterations+1):
            number_of_operations=1000*j
            matrix_size=100*i
            a=MatrixGenerator(matrix_size)

            start = time.time()
            a.generate_matrices(number_of_operations)
            end = time.time()
    #        print(a.ENmatrix)
            ones_perc=matrix_stats(a.ENmatrix, a.size, number_of_operations)
            del a
            print("Generation time:", end - start)
            print("\n")
            y_lst.append(number_of_operations)
            time_lst.append(end-start)
            ones_perc_list.append(ones_perc)
        plot_analysis(time_lst, y_lst, matrix_size, ones_perc_list)


'''Right now returning ones percentage in the matrix and writing a lot of info'''
def matrix_stats(matrix, size, number_of_operations): #returns ones percentage
    ones=0
    for i in range(size):
        for j in range (size):
            if matrix[i][j]==1:
                ones+=1
    print("Matrix size:", size)
    print("Matrix elements:", size*size)
    print("Number of elementary operations:", number_of_operations)
    print("Ones (1) in the matrix:", ones)
    print("Zeros (0) in the matrix:", size*size-ones)
    print("Ones percentage in the matrix", 100*ones/(size*size))

    return 100*ones/(size*size)

'''Manages several plots, legend and points labels'''
def plot_analysis(time_lst, y_lst, matrix_size, ones_perc_list):
    line, = plt.plot(y_lst, time_lst, '-o', label=str(matrix_size)+"x"+str(matrix_size))
    i=0
    for x,y in zip(y_lst,time_lst):
        plt.annotate(round(ones_perc_list[i],2), (x,y), textcoords="offset points",xytext=(0,10),ha='center')
        i+=1


    plots.append(line,)





plots=[]
test(10, 10)

plt.xlabel("Number of operations [number]")
plt.ylabel("Time [s]")
plt.title("Matrix generation time depending on size and number of operations\n Numbers above points indicate percentage of ones (1) in a certain matrix")
plt.legend(handles=plots[::-1], title="Matrix size")
plt.show()
