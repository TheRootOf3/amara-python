class ENDECrytpion():
    def __init__(self, size):
        self.size=size

    def ende_crypt(self, message, matrix):
        endecrypted_message=[]
        helplist=[]
        for a in message:
            helplist=[0 for x in range(self.size)]
            for i in range(len(a)):
                if a[i]==1:
                     helplist=list(map(lambda a, b : (a+b)%2, helplist, matrix[i]))
            endecrypted_message.append(helplist)

        return endecrypted_message
