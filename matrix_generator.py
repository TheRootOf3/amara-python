'''This file contains all functions for matrix generation'''

import random as random
import operator as operator

class MatrixGenerator():
    '''generating binary matrices with 1 on diagonal, 0 everywhere else'''
    def __init__(self, size):
        self.size=size
        self.ENmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]
        self.DEmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]

        self.history_matrix=[] #[bool operation type(False - addition, True - swap), int row1 number, int row2 number]

    '''
    Making an random unit operation on ENMatrix- xor of two rows or swap of two rows
    and storing operation type and changed rows to history_matrix list in the format noted above
    '''
    def ENunit_operation(self):
        row1_num = random.randint(0,self.size-1)
        row2_num = random.randint(0,self.size-1)

        while(row1_num==row2_num):
            row2_num = random.randint(0,self.size-1)

        if not row1_num%2:
            self.ENmatrix[row1_num]=self.add_rows_map(row1_num, row2_num, self.ENmatrix)
            self.history_matrix.append([False, row1_num, row2_num])
        else:
            self.ENmatrix[row1_num], self.ENmatrix[row2_num] = self.swap_rows(row1_num, row2_num, self.ENmatrix)
            self.history_matrix.append([True, row1_num, row2_num])

    '''
    Creating a DEMatrix using operations saved in history_matrix but in a reversed order
    '''
    def DEunit_operation(self):
        if not self.history_matrix[-1][0]:
            self.DEmatrix[self.history_matrix[-1][1]]=self.add_rows_map(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)
        else:
            self.DEmatrix[self.history_matrix[-1][1]], self.DEmatrix[self.history_matrix[-1][2]] = self.swap_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)

        del self.history_matrix[-1]

    '''
    Function for adding two rows (xor)
    maping using operator.xor turned out to be faster than lambda sum%2
    '''
    def add_rows_map(self, row1_num, row2_num, matrix):
        #return list(map(lambda a, b : (a+b)%2, matrix[row1_num], matrix[row2_num])) #Saving addition result on the first row num
        return list(map(operator.xor, matrix[row1_num], matrix[row2_num])) #operator.xor optimizes code #Saving addition result on the first row num

    '''
    Returning rows swaped
    '''
    def swap_rows(self, row1_num, row2_num, matrix):
        if matrix[row1_num]!=matrix[row2_num]:
            return matrix[row2_num], matrix[row1_num]

    '''
    Function performing given number of unit operations on both EN and DE matrices
    '''
    def generate_matrices(self, operation_num):
        for i in range(operation_num):
            self.ENunit_operation()
        for i in range(operation_num):
            self.DEunit_operation()
