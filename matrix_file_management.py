from message_modifier import *

class MatrixFileManagement():
    @staticmethod
    def matrix_to_file(filename, matrix, size):
        with open(filename, 'w') as f:
            f.write(str(size))
            f.write("\n")
            f.write(MessageModifier.list_to_string(matrix))

    @staticmethod
    def file_to_matrix(filename):
        matrix=[]
        with open(filename, 'r') as f:
            size=int(f.readline())
            matrix_string=f.readline()
            matrix=[[int(x) for x in matrix_string[i*size:(i+1)*size]] for i in range (size)]

        return matrix, size
