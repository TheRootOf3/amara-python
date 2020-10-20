import random as random
import operator as operator
import cProfile

class Matrix():
    def __init__(self, size):
        self.size=size
        self.ENmatrix=[[(True if j==i else False) for j in range(0,size)] for i in range(0,size)]
        self.DEmatrix=[[(True if j==i else False) for j in range(0,size)] for i in range(0,size)]

        self.history_matrix=[] #[bool operation type(False - addition, True - swap), int row1 number, int row2 number]

    def ENunit_operation(self):
        self.row1_num = random.randint(0,self.size-1)
        self.row2_num = random.randint(0,self.size-1)

        while(self.row1_num==self.row2_num):
            self.row2_num = random.randint(0,self.size-1)

        if not self.row1_num%2:
            self.add_rows_map(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([False, self.row1_num, self.row2_num])
        else:
            self.swap_rows(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([True, self.row1_num, self.row2_num])

    def DEunit_operation(self):
        if not self.history_matrix[-1][0]:
            self.add_rows_map(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)
        else:
            self.swap_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)

        del self.history_matrix[-1]

    def add_rows_map(self, row1_num, row2_num, matrix):
        matrix[row1_num]=list(map(operator.xor, matrix[row1_num], matrix[row2_num])) #Saving addition result on the first row num

    def swap_rows(self, row1_num, row2_num, matrix):
        if matrix[row1_num]!=matrix[row2_num]:
            matrix[row1_num], matrix[row2_num]=matrix[row2_num], matrix[row1_num]

class Message():
    def __init__(self, matrixobject):
        self.size=matrixobject.size
        self.bool_message=[]

    def CharToBool(self, char):
        return [bool(int(x)) for x in (format(ord(char), 'b'))]

    def MessageToBool(self, message):
        for char in message:
            self.bool_message+=(self.CharToBool(char))

    def ReshapeBoolList(self):
        self.reshaped_bool_message=[]

        if len(self.bool_message)%self.size!=0:
            for i in range (0,(len(self.bool_message)//self.size)):
                self.reshaped_bool_message.append(self.bool_message[(i)*self.size:self.size*(i+1)])

            last_frag=self.bool_message[(len(self.bool_message)//self.size)*self.size:]
            while len(last_frag) < self.size:
                last_frag.append(False)
            self.reshaped_bool_message.append(last_frag)

        else:
            for i in range (0,(len(self.bool_message)//self.size)):
                self.reshaped_bool_message.append(self.bool_message[(i)*self.size:self.size*(i+1)])


a=Matrix(100)
m=Message(a)
m.MessageToBool("Hello World!")
m.ReshapeBoolList()

# print(len(m.bool_message))
# print(m.bool_message)
# print(m.reshaped_bool_message)
# print(len(m.reshaped_bool_message[0]))



#for i in range (30000):
#     a.ENunit_operation()
#     print(a.history_matrix)
#     print("\n")
#for i in range (30000):
#     a.DEunit_operation()
#     print(a.history_matrix)
#     print("\n")

#print(a.entry_matrix)
#print(a.ENmatrix)
#print(a.DEmatrix)
