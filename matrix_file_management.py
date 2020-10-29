'''This file contains all functions for file management'''

from message_modifier import *

class FileManagement():
    '''
    Saving file to matrix in format:
    1st line - size of the matrix
    2nd line - all matrix elements
    '''
    @staticmethod
    def matrix_to_file(filename, matrix, size):
        with open(filename, 'w') as f:
            f.write(str(size))
            f.write("\n")
            f.write(MessageModifier.list_to_string(matrix))

    '''
    Reading file to matrix in format:
    1st line - size of the matrix -> int size
    2nd line - all matrix elements -> list of lists of ints matrix
    '''
    @staticmethod
    def file_to_matrix(filename):
        matrix=[]
        with open(filename, 'r') as f:
            size=int(f.readline())
            matrix_string=f.readline()
            matrix=[[int(x) for x in matrix_string[i*size:(i+1)*size]] for i in range (size)]

        return matrix, size

    '''
    Writes to a file in format:
    1st line - all values
    '''
    @staticmethod
    def write_to_file(filename, message_string):
        with open(filename, 'w') as f:
            f.write(message_string)

    '''
    Reads a file in format:
    All lines
    '''
    @staticmethod
    def read_file(filename):
        message_string=""
        with open(filename, 'r') as f:
             for line in f.readlines():
                 message_string+=(line)
        return message_string
