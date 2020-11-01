'''This file contains all functions for running the complete program'''

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

    ''' reading matrices from file/generating matrices mode selection function'''
    def runmode_matrix(self):
        if int(input("runmode: 0 - generate matrices, 1 - load matrices from file: "))==0:
            self.size=int(input("Choose matrix size: "))
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
            self.DEmatrix, self.size = FileManagement.file_to_matrix("privatekey.txt")
            self.ENmatrix, self.size = FileManagement.file_to_matrix("publickey.txt")

    '''
    mode selection function
    0 - encrypt from terminal window
    1 - decrypt from terminal window
    2 - encrypt and decrypt from terminal window
    3 - encrypt a file <given filename> to a new file with name encr_<given filename>
    4 - decrypt a file <given filename> to a new file with name decr_<given filename>
    '''
    def runmode_action(self):
        input_mode=None
        input_mode=int(input("runmode: 0 - encrypt, 1 - decrypt, 2 - both, 3 - encrypt a file, 4 - decrypt a file: "))

        if input_mode==0:
            self.encrypt(input("Message to encrypt (characters): ")) #ASCII string

        elif input_mode==1:
            self.decrypt(input("Messege to decrypt (binary values (0,1) sequence): ")) #binary values (0,1) string

        elif input_mode==3:
            filename=input("File name: ")
            file_input=FileManagement.read_file(filename)
            file_output=self.m.list_to_string(self.encrypt_file(file_input))

            FileManagement.write_to_file("encr_"+filename, file_output)

        elif input_mode==4:
            filename=input("File name: ")
            file_input=FileManagement.read_file(filename)
            file_output=self.m.list_to_string(self.decrypt_file(file_input))

            FileManagement.write_to_file("decr_"+filename[5:] if filename[0:5]=="encr_" else "decr_"+filename, file_output)

        else:
            self.encrypt(input("Message to encrypt (characters): ")) #ASCII string
            self.decrypt(input("Messege to decrypt (binary values (0,1) sequence): ")) #binary values (0,1) string

    '''Encrypting function: reshaping message, then encrypting'''
    def encrypt(self, input):
        bool_message=self.m.messageToBin(input+"\x03") #Adding ETX (end of text) char in order to decrypt correctly
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

    '''Decrypting function: reshaping message, then decrypting'''
    def decrypt(self, input):
        decrypted=self.ende.ende_crypt(self.m.reshapeBinList([int(x) for x in input]), self.DEmatrix)
        # print("\n")
        # print(decrypted)
        # print("\n")
        # print("Decrypted:\n",self.m.list_to_string(decrypted))
        print("\nDecrypted text message:")
        print(self.m.messageToText(decrypted))

    def encrypt_file(self, input):
        bool_message=self.m.messageToBin(input+"\x03")
        reshaped_message=self.m.reshapeBinList(bool_message)
        return self.ende.ende_crypt(reshaped_message, self.ENmatrix)

    def decrypt_file(self, input):
        return self.m.messageToText(self.ende.ende_crypt(self.m.reshapeBinList([int(x) for x in input]), self.DEmatrix))

    '''Saving (overwrting) matrices to files, name publickey.txt, privatekey.txt'''
    def save_matrices(self):
       FileManagement.matrix_to_file("publickey.txt", self.ENmatrix, self.size)
       FileManagement.matrix_to_file("privatekey.txt", self.DEmatrix, self.size)

r=Run()
