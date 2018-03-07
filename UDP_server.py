'''
Created on Mar 3, 2018

@author: jessjab
'''
import socket
import sys
#Decrypting the input file with the given key______________________________________________________________________________
def FlipandXOR_decode(key,data):
    i=0    
    dataLeft =0
    dataRight =0
    dataRight_new =0
    datLeft_new =0
    string = ""
    temp_st = ""
    
    print "Original Data:", data
    for i in range(0,len(data)):
        #print data[i]
        if i == len(data)-1 and i % 2 == 0:
            dataLeft = ord(data[i])
            dataRight_new = chr(dataLeft ^int(key))
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
            
            dataRight_new = str(chr(dataLeft))
            #print "dataRight_new: ", dataRight_new
            dataLeft_new = str(chr(dataRight ^key))
            #print "dataLeft_new: ",dataLeft_new
            
            temp_st = dataLeft_new + dataRight_new
            #print "the temp is:", temp_st
            string = string + temp_st
        #print "String", string

    return string

if __name__ == '__main__':
    pass

#Retrieving data from user_______________________________________________________________________________________
    if(len(sys.argv)-1 !=1):
        print "Incorrect number of arguments.(",len(sys.argv)-1, ")" 
        print "Enter: port number"
        sys.exit()
    UDP_PORT_NO = sys.argv[1]
    UDP_PORT_NO_int = int(UDP_PORT_NO)
#     ENCRYPT_KEY= sys.argv[2]
    ENCRYPT_KEYS= [0,1,2,3,4]
    #ENCRYPT_KEY= 5
    
    print "You entered: ",UDP_PORT_NO_int
    
    
    
    #Retrieving Server IP Address_____________________________________________________________________________________
    S = socket.socket()
    UDP_HOST_NAME =socket.gethostname()
    SERVER_IP_ADDRESS=socket.gethostbyname(UDP_HOST_NAME)
    SERVER_IP_ADDRESS = "127.0.0.1"
    
    
    #Receiving data from Client and decrypting message_________________________________________________________________________________________
    UDP_STORED_MESSAGES = ["", "", "","", ""]
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((SERVER_IP_ADDRESS , UDP_PORT_NO_int))
    while True:
        print >>sys.stderr, 'waiting to receive message from client'
        CLIENT_DATA, ADDR = serverSock.recvfrom(1024)
        CLIENT_DATA_split = CLIENT_DATA.split()
        ENCODED_MESSAGE =" ".join(CLIENT_DATA_split[6:])
        
        CLIENT_NUMBER = CLIENT_DATA_split[1]
        print "Client Number: ", CLIENT_NUMBER
        print "Length of encrypted keys", len(ENCRYPT_KEYS)
        if CLIENT_NUMBER <= len(ENCRYPT_KEYS):
            print "The Key for this client is not available."
            sys.exit()
            
        DECODED_MESSAGE = FlipandXOR_decode(ENCRYPT_KEYS[int(CLIENT_NUMBER)], ENCODED_MESSAGE)
        #print "encoded: ", ENCODED_MESSAGE
        #print "decoded: ",DECODED_MESSAGE
        CLIENT_DATA_BACK = CLIENT_DATA.replace(ENCODED_MESSAGE,DECODED_MESSAGE)
        
        print >>sys.stderr, 'received %s bytes from %s' % (len(CLIENT_DATA), ADDR)
        #print >>sys.stderr, CLIENT_DATA
        print "Server received message from client: ", CLIENT_DATA
        print "Server received message from client and DECRYPTED IT: ",DECODED_MESSAGE
        
     #Sending last 5 stored messages to Client______________________________________________________________________________________________   
        if CLIENT_DATA:
            for i in range(len(UDP_STORED_MESSAGES)-1,0,-1):
                UDP_STORED_MESSAGES[i] =UDP_STORED_MESSAGES[i-1]
                
            UDP_STORED_MESSAGES[0] = CLIENT_DATA_BACK
            print "Last 5 Messages:", UDP_STORED_MESSAGES
            
            sent = serverSock.sendto(str(UDP_STORED_MESSAGES),ADDR)
            print >>sys.stderr, 'sent %s bytes back to %s' % (sent, ADDR)
            #print >>sys.stderr, 'Sent message to client', UDP_STORED_MESSAGES
        