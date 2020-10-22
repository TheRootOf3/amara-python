import random as random
import operator as operator

class MatrixGenerator():
    def __init__(self, size):
        self.size=size
        self.ENmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]
        self.DEmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]

        self.history_matrix=[] #[bool operation type(False - addition, True - swap), int row1 number, int row2 number]

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

    def DEunit_operation(self):
        if not self.history_matrix[-1][0]:
            self.DEmatrix[self.history_matrix[-1][1]]=self.add_rows_map(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)
        else:
            self.DEmatrix[self.history_matrix[-1][1]], self.DEmatrix[self.history_matrix[-1][2]] = self.swap_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)

        del self.history_matrix[-1]

    def add_rows_map(self, row1_num, row2_num, matrix):
        #return list(map(lambda a, b : (a+b)%2, matrix[row1_num], matrix[row2_num])) #Saving addition result on the first row num
        return list(map(operator.xor, matrix[row1_num], matrix[row2_num])) #operator.xor optimizes code #Saving addition result on the first row num
    def swap_rows(self, row1_num, row2_num, matrix):
        if matrix[row1_num]!=matrix[row2_num]:
            return matrix[row2_num], matrix[row1_num]

    def generate_matrices(self, operation_num):
        for i in range(operation_num):
            self.ENunit_operation()
        for i in range(operation_num):
            self.DEunit_operation()
