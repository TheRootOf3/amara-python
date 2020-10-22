import time as time
from matrix_generator import *
from message_modifier import *
from ENDE_cryption_algo import *
from matrix_file_management import *


class Run():
    def __init__(self):
        self.size=0
        self.runmode_matrix()

        if self.size!=0:
            self.m=MessageModifier(self.size)
            self.ende=ENDECrytpion(self.size)
            self.runmode_action()

            # reading matrices from file/generating matrices mode selection
    def runmode_matrix(self):
        if int(input("runmode: 0 - generate matrices, 1 - load matrices from file: "))==0:
            self.size=int(input("Choose matrix size (cannot be n%3==2): "))
            while(self.size%3==2):
                self.size=int(input("Choose matrix size (cannot be n%3==2): "))
            number_of_operations=int(input("Choose number of elementary operations: "))
            start = time.time()
            self.a=MatrixGenerator(self.size)
            self.a.generate_matrices(number_of_operations)
            self.ENmatrix=self.a.ENmatrix
            self.DEmatrix=self.a.DEmatrix
            end = time.time()
            print("Matrix generation elapsed time:", end-start)

            if input("Generated matrices. Save(y/n)?")=='y':
                self.save_matrices()
        else:
            self.DEmatrix, self.size = MatrixFileManagement.file_to_matrix("privatekey.txt")
            self.ENmatrix, self.size = MatrixFileManagement.file_to_matrix("publickey.txt")

            # encryption/decryption/both mode selection
    def runmode_action(self):
        input_mode=None
        input_mode=int(input("runmode: 0 - encrypt, 1 - decrypt, 2 - both: "))
        if input_mode==0:
            self.encrypt(input("Message to encrypt: ")) #ASCII string
        elif input_mode==1:
            self.decrypt(input("Messege to decrypt: ")) #binary values (0,1) string
        else:
            self.encrypt(input("Message to encrypt: ")) #ASCII string
            self.decrypt(input("Messege to decrypt: ")) #binary values (0,1) string


    def encrypt(self, input):
        bool_message=self.m.messageToBin(input+"\x03") #Adding ETX char in order to decrypt correctly
        # print("Message in a bool format:")
        # print(bool_message)
        # print("\n")
        reshaped_message=self.m.reshapeBinList(bool_message)
        # print("Message in a bool format reshaped to matrix size:")
        # print(reshaped_message)
        encrypted=self.ende.ende_crypt(reshaped_message, self.ENmatrix)
        print("\nEncrypted:")
        print(self.m.list_to_string(encrypted))
        print("\n")

    def decrypt(self, input):
        decrypted=self.ende.ende_crypt(self.m.reshapeBinList([int(x) for x in input]), self.DEmatrix)
        # print("\n")
        # print(decrypted)
        # print("\n")
        # print("Decrypted:\n",self.m.list_to_string(decrypted))
        print("\nDecrypted text message:")
        print(self.m.messageToText(decrypted))

    def save_matrices(self):
       MatrixFileManagement.matrix_to_file("publickey.txt", self.ENmatrix, self.size)
       MatrixFileManagement.matrix_to_file("privatekey.txt", self.DEmatrix, self.size)

r=Run()
