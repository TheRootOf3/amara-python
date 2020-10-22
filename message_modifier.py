class MessageModifier():
    def __init__(self, size):
        self.size=size

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

    @staticmethod
    def list_to_string(list):
        string=""
        for i in list:
            for j in i:
                string+=str(j)
        return string

    def cut_zeros(self,string):
        return string[:len(string)-len(string)%8]

    def messageToText(self, message):
        message=self.list_to_string(message)
        final_message=""
        i=0
        final_message+=(self.binToChar(message[i*8:(i+1)*8]))
        i+=1
        while(final_message[-1]!="\x03"): #checking where is "\x03" (ETX) in the messege and stops conversion
            final_message+=(self.binToChar(message[i*8:(i+1)*8]))
            i+=1

        return final_message[:-1]
