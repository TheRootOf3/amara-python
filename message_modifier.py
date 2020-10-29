'''This file contains all functions for message reshaping'''

class MessageModifier():
    def __init__(self, size):
        self.size=size
    '''
    converting char to bin in ASCII 8 bit format (a= 01100001)
    saving each char as an 8 element list
    '''
    def charToBin(self, char):
        return [int(x) for x in '{0:08b}'.format(ord(char))]

    '''converting bin value to char'''
    def binToChar(self, bin):
        return chr(int(bin, 2))

    '''converting whole message to bin format -> saving it as a list of lists of length 8'''
    def messageToBin(self, message):
        bool_message=[]
        for char in message:
            bool_message+=(self.charToBin(char))

        return bool_message

    '''Reshaping message from list of lists of length 8 to list of lists of length size!'''
    def reshapeBinList(self, bool_message):
        reshaped_bool_message=[]
        if len(bool_message)%self.size!=0:
            for i in range (0,(len(bool_message)//self.size)):
                reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

            last_frag=bool_message[(len(bool_message)//self.size)*self.size:]
            reshaped_bool_message.append(last_frag)

        else:
            for i in range (0,(len(bool_message)//self.size)):
                reshaped_bool_message.append(bool_message[(i)*self.size:self.size*(i+1)])

        return reshaped_bool_message

    '''function also used in matrix_file_management file'''
    @staticmethod
    def list_to_string(list):
        string=""
        for i in list:
            for j in i:
                string+=str(j)
        return string

    '''
    This function converts a binary sequency to a text
    It works only if text was encoded using char to bin function
    1 letter = 1 byte (a= 01100001)
    '''
    def messageToText(self, message):
        message=self.list_to_string(message)
        final_message=""
        i=0
        final_message+=(self.binToChar(message[i*8:(i+1)*8])) #!!! 1 letter = 1 byte
        i+=1
        while(final_message[-1]!="\x03"): #checking where is "\x03" (ETX) in the messege and stops conversion
            final_message+=(self.binToChar(message[i*8:(i+1)*8]))
            i+=1

        return final_message[:-1]
