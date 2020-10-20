import numpy as np
import random as random
import time


import cProfile

class Matrix():
    def __init__(self, size):
        self.size=size

        self.entry_matrix=np.zeros((size,size), bool)
        np.fill_diagonal(self.entry_matrix, True)

        self.ENmatrix=self.entry_matrix.copy()
        self.DEmatrix=self.entry_matrix.copy()

        self.history_matrix=[] #[bool operation type(False - addition, True - swap), int row1 number, int row2 number]

    def ENunit_operation(self):
        self.row1_num = random.randint(0,self.size-1)
        self.row2_num = random.randint(0,self.size-1)
        while(self.row1_num==self.row2_num):
            self.row2_num = random.randint(0,self.size-1)

        if not random.randint(0,1):
            self.add_rows(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([False, self.row1_num, self.row2_num])
        else:
            self.swap_rows(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([True, self.row1_num, self.row2_num])

    def DEunit_operation(self):
        #if len(self.history_matrix)>0:
        if not self.history_matrix[-1][0]:
            self.add_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)
        else:
            self.swap_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)

        del self.history_matrix[-1]

    def add_rows(self, row1_num, row2_num, matrix):
        for i in range (self.size):
            matrix[row1_num][i]=(matrix[row1_num][i]!=matrix[row2_num][i]) #Saving addition result on the first row num

    def swap_rows(self, row1_num, row2_num, matrix):
        for i in range (self.size):
            if matrix[row1_num][i]!=matrix[row2_num][i]:
                matrix[row1_num][i], matrix[row2_num][i]=\
                matrix[row2_num][i], matrix[row1_num][i]


a=Matrix(1000)

for i in range (3000):
     a.ENunit_operation()
#for i in range (3000):
#     a.DEunit_operation()

print(a.ENmatrix)
print(a.DEmatrix)
