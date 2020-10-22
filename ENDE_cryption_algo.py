import time as time
import operator as operator

class ENDECrytpion():
    def __init__(self, size):
        self.size=size

    def ende_crypt(self, message, matrix):
        endecrypted_message=[]
        helplist=[]
        start=time.time()
        for a in message:
            helplist=[0 for x in range(self.size)]
            for i in range(len(a)):
                if a[i]==1:
                     # helplist=list(map(lambda a, b : (a+b)%2, helplist, matrix[i]))
                     helplist=list(map(operator.xor, helplist, matrix[i])) #operator.xor optimizes code
            endecrypted_message.append(helplist)
        end=time.time()
        print("encryption/decryption elapsed time:", end-start)
        return endecrypted_message
