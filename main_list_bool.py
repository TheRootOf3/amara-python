import random as random

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
            self.ENmatrix[self.row1_num]=self.add_rows_map(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([False, self.row1_num, self.row2_num])
        else:
            self.ENmatrix[self.row1_num], self.ENmatrix[self.row2_num] = self.swap_rows(self.row1_num, self.row2_num, self.ENmatrix)
            self.history_matrix.append([True, self.row1_num, self.row2_num])

    def DEunit_operation(self):
        if not self.history_matrix[-1][0]:
            self.DEmatrix[self.history_matrix[-1][1]]=self.add_rows_map(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)
        else:
            self.DEmatrix[self.history_matrix[-1][1]], self.DEmatrix[self.history_matrix[-1][2]] = self.swap_rows(self.history_matrix[-1][1], self.history_matrix[-1][2], self.DEmatrix)

        del self.history_matrix[-1]

    def add_rows_map(self, row1_num, row2_num, matrix):
        return list(map(operator.xor, matrix[row1_num], matrix[row2_num])) #Saving addition result on the first row num

    def swap_rows(self, row1_num, row2_num, matrix):
        if matrix[row1_num]!=matrix[row2_num]:
            return matrix[row2_num], matrix[row1_num]

    def generate_matrices(self, operation_num):
        for i in range(operation_num):
            self.ENunit_operation()
        for i in range(operation_num):
            self.DEunit_operation()



class Message():
    def __init__(self, matrixobject):
        self.matrixobject=matrixobject
        self.size=self.matrixobject.size
        self.bool_message=[]

    def CharToBool(self, char):
        return [bool(int(x)) for x in (format(ord(char), 'b'))]

    def MessageToBool(self, message):
        for char in message:
            self.bool_message+=(self.CharToBool(char))

        return self.bool_message

    def ReshapeBoolList(self, bool_message):
        self.reshaped_bool_message=[]

        if len(bool_message)%self.size!=0:
            for i in range (0,(len(bool_message)//self.size)):
                self.reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

            last_frag=bool_message[(len(bool_message)//self.size)*self.size:]

            #think about if False addition has any sense!!!
#            while len(last_frag) < self.size:
#                last_frag.append(False)

            self.reshaped_bool_message.append(last_frag)

        else:
            for i in range (0,(len(bool_message)//self.size)):
                self.reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

        return self.reshaped_bool_message

    def ENDECrypt(self, message, matrix):
        self.endecrypted_message=[]
        self.helplist=[]
        for a in message:
            self.helplist=[False for x in range(self.size)]
            for i in range(len(a)):
                if a[i]==True:
                     self.helplist=list(map(operator.xor, self.helplist, matrix[i]))
            self.endecrypted_message.append(self.helplist)

        return self.endecrypted_message




a=Matrix(3)
a.generate_matrices(10)
m=Message(a)
bool_message=m.MessageToBool("a")
print("Message in bool format:\n",bool_message,"\n")
reshaped_message=m.ReshapeBoolList(bool_message)
print("Message in bool format reshaped to matrix size:\n",reshaped_message,"\n")
encrypted=m.ENDECrypt(reshaped_message, a.ENmatrix)
print("Encrypted:\n",encrypted)
decrypted=m.ENDECrypt(encrypted, a.DEmatrix)
print("Decrypted:\n",decrypted)
print("\n")
print("\n")
print("ENM:\n",a.ENmatrix)
print("DEM:\n",a.DEmatrix)





# a=Matrix(3)
# m=Message(a)
# m.MessageToBool("a")
# m.ReshapeBoolList()
# print(m.reshaped_bool_message)
# # print(len(m.bool_message))
# # print(m.bool_message)
# # print(m.reshaped_bool_message)
# # print(len(m.reshaped_bool_message))
# # print(len(m.bool_message))
# for i in range (10):
#      a.ENunit_operation()
# #     print(a.history_matrix)
# #     print("\n")
# for i in range (10):
#      a.DEunit_operation()
# #     print(a.history_matrix)
# #     print("\n")
# m.ENDECrypt(m.reshaped_bool_message,a.ENmatrix)
# print(m.endecrypted_message)
# print("\n")
# #print(a.entry_matrix)
# print(a.ENmatrix)
# print(a.DEmatrix)
# print("\n")
# m.ENDECrypt(m.endecrypted_message,a.DEmatrix)
# print(m.endecrypted_message)
