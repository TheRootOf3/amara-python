import random as random

class Matrix():
    def __init__(self, size):
        self.size=size
        self.ENmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]
        self.DEmatrix=[[(1 if j==i else 0) for j in range(0,size)] for i in range(0,size)]

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
        return list(map(lambda a, b : (a+b)%2, matrix[row1_num], matrix[row2_num])) #Saving addition result on the first row num

    def swap_rows(self, row1_num, row2_num, matrix):
        if matrix[row1_num]!=matrix[row2_num]:
            return matrix[row2_num], matrix[row1_num]

    def generate_matrices(self, operation_num):
        for i in range(operation_num):
            self.ENunit_operation()
        for i in range(operation_num):
            self.DEunit_operation()

class MatrixFileManagement():
    def __init__(self, messageobj):
        self.messageobj=messageobj

    def matrix_to_file(self, filename, matrix):
        with open(filename, 'a+') as f:
            f.write(str(self.messageobj.size))
            f.write("\n")
            f.write(self.messageobj.list_to_string(matrix))

    def file_to_matrix(self, filename):
        self.matrix=[]
        with open(filename, 'r') as f:
            self.size=int(f.readline())
            self.matrix_string=f.readline()
            for i in range(self.size):
                self.matrix.append([int(x) for x in self.matrix_string[i*self.size:(i+1)*self.size]])

        return self.matrix


class Message():
    def __init__(self, matrixobject):
        self.matrixobject=matrixobject
        self.size=self.matrixobject.size

    def charToBin(self, char):
        return [int(x) for x in '{0:08b}'.format(ord(char))]

    def binToChar(self, bin):
        return chr(int(bin, 2))

    def messageToBin(self, message):
        self.bool_message=[]
        for char in message:
            self.bool_message+=(self.charToBin(char))

        return self.bool_message

    def reshapeBinList(self, bool_message):
        self.reshaped_bool_message=[]

        if len(bool_message)%self.size!=0:
            for i in range (0,(len(bool_message)//self.size)):
                self.reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

            last_frag=bool_message[(len(bool_message)//self.size)*self.size:]
            self.reshaped_bool_message.append(last_frag)

        else:
            for i in range (0,(len(bool_message)//self.size)):
                self.reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

        return self.reshaped_bool_message

    def list_to_string(self, list):
        string=""
        for i in list:
            for j in i:
                string+=str(j)
        return string

    def cut_zeros(self,string):
        return string[:len(string)-len(string)%8]

    def messageToText(self, message):
        self.message=self.cut_zeros(self.list_to_string(message))
        self.final_message=""
        for i in range(len(self.message)//8):
            self.final_message+=(self.binToChar(self.message[i*8:(i+1)*8]))

        return self.final_message

class ENDECrytpion():
    def __init__(self, matrixobject):
        self.matrixobject=matrixobject
        self.size=self.matrixobject.size


    def ende_crypt(self, message, matrix):
        self.endecrypted_message=[]
        self.helplist=[]
        for a in message:
            self.helplist=[0 for x in range(self.size)]
            for i in range(len(a)):
                if a[i]==1:
                     self.helplist=list(map(lambda a, b : (a+b)%2, self.helplist, matrix[i]))
            self.endecrypted_message.append(self.helplist)

        return self.endecrypted_message


class Run():
    def __init__(self, runmode): #runmode: 0 - generate matrices, 1 - load matrices from file
        self.a=Matrix(100)
        self.m=Message(self.a)
        self.ende=ENDECrytpion(self.a)
        self.mfm=MatrixFileManagement(self.m)
        if runmode==0:
            self.a.generate_matrices(3000)
            if input("Generated matrices. Save(y/n)?")=='y':
                self.save_matrices()
        else:
            self.a.DEmatrix=self.mfm.file_to_matrix("privatekey.txt")
            self.a.ENmatrix=self.mfm.file_to_matrix("publickey.txt")



        self.encrypt(input("Message to encrypt: ")) #ASCII string
        self.decrypt(input("Messege to decrypt: ")) #binary values (0,1) string

    def encrypt(self, input):
        self.bool_message=self.m.messageToBin(input)
        print("Message in a bool format:\n",self.bool_message,"\n")
        self.reshaped_message=self.m.reshapeBinList(self.bool_message)
        print("Message in a bool format reshaped to matrix size:\n",self.reshaped_message,"\n")
        self.encrypted=self.ende.ende_crypt(self.reshaped_message, self.a.ENmatrix)
        print("Encrypted:\n",self.m.list_to_string(self.encrypted))
    def decrypt(self, input):
        self.decrypted=self.ende.ende_crypt(self.m.reshapeBinList([int(x) for x in input]), self.a.DEmatrix)
        print("Decrypted:\n",self.m.list_to_string(self.decrypted))
        print("\n")
        print("\n")
        print(self.m.messageToText(self.decrypted))

    def save_matrices(self):
       self.mfm.matrix_to_file("publickey.txt", self.a.ENmatrix)
       self.mfm.matrix_to_file("privatekey.txt", self.a.DEmatrix)



r=Run(int(input("runmode: 0 - generate matrices, 1 - load matrices from file:")))
