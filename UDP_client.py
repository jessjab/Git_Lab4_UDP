'''
Created on Mar 3, 2018

@author: jessjab
'''
import sys
import socket
import time
import datetime;
from time import gmtime,strftime

#Encrypting the input file with the given key______________________________________________________________________________
def FlipandXOR(key,data):
    i=0    
    dataLeft =0
    dataRight =0
    dataRight_new =0
    datLeft_new =0
    string = ""
    temp_st = ""
 
    for i in range(0,len(data)):
        #print data[i]
        if i == len(data)-1 and i % 2 == 0:
            dataLeft = ord(data[i])
            dataRight_new = chr(dataLeft ^int( ENCRYPT_KEY))
            string = string +str(dataRight_new)
            #print "Encrypted Data",string 
            
        elif i %2 ==0:
            dataLeft = ord(data[i])
            #print "i: ",i
        elif i %2 !=0:
            dataRight = ord(data[i])
        
#             print "i:", i
            #print "dataRightOld: ", chr(dataRight)
            #print "dataLeftOld: ", chr(dataLeft)
            
            dataRight_new = str(chr(dataLeft ^int( ENCRYPT_KEY)))
            #print "dataRight_new: ", dataRight_new
            dataLeft_new = chr(dataRight)
            #print "dataLeft_new: ",dataLeft_new
            
            temp_st = dataLeft_new + dataRight_new
            #print "the temp is:", temp_st
            string = string + temp_st
    print "Encrypted Data: ",string 

    return string


if __name__ == '__main__':
    pass
    #Retrieving data from user___________________________________________________________________________________________
    if(len(sys.argv)-1 !=4):
        print "Incorrect number of arguments.(",len(sys.argv)-1, ")" 
        print "Enter: Servers IP address, port number, encryption key, and input file message. "
        sys.exit()
    
    SERVER_IP_ADDRESS = sys.argv[1]
    UDP_PORT_NO = sys.argv[2]
    UDP_PORT_NO_int = int(UDP_PORT_NO)
    CLIENT_NUMBER= sys.argv[3]
    ENCRYPT_KEY= sys.argv[4]
    INPUT_MESSAGE = raw_input("input: ")

    print "You entered: ", SERVER_IP_ADDRESS, UDP_PORT_NO_int,ENCRYPT_KEY, "and Message:", INPUT_MESSAGE

    ENCRYPTED_MESSAGE =FlipandXOR(ENCRYPT_KEY, INPUT_MESSAGE)       
        
    #Retrieving Client IP Address_____________________________________________________________________________________
    S = socket.socket()
    UDP_HOST_NAME =socket.gethostname()
    CLIENT_IP_ADDRESS=socket.gethostbyname(UDP_HOST_NAME)
    #print ("Your Computer Name is: " + UDP_HOST_NAME)
    #print ("Your Computer IP Address is: " +CLIENT_IP_ADDRESS)
    
    #Retrieving Client Timestamp_____________________________________________________________________________________
    DATE = strftime("Date_Sent:%m-%d-%Y", gmtime())
    TIME = datetime.datetime.time(datetime.datetime.now())
    TIMESTAMP = str(DATE)+ " Time_Sent:" +str(TIME)
    #print TIMESTAMP
    
    #Sending data to Server__________________________________________________________________________________________
    MESSAGE_TO_SEND = "Client:# " + CLIENT_NUMBER + " " +TIMESTAMP + " Client_IP_Address:" + CLIENT_IP_ADDRESS + " Message: " +ENCRYPTED_MESSAGE
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = clientSock.sendto(MESSAGE_TO_SEND, (SERVER_IP_ADDRESS, UDP_PORT_NO_int))
    print >>sys.stderr, 'sent %s bytes to %s' % (sent, SERVER_IP_ADDRESS)
    
    #Receiving data from Server______________________________________________________________________________________
    while True:
        print >>sys.stderr, 'waiting to receive message from server'
        DATA_BACK, ADDR = clientSock.recvfrom(1024)
        print >>sys.stderr, 'received %s bytes back from %s' % (len(DATA_BACK), ADDR)
        print "Client received message from server: ", DATA_BACK
        break
