# coding : utf-8

biao = set()
with open("keywords", "r", encoding="utf-8") as f:
    for line in f.readlines():
        word = line.replace("\n", "")
        if word not in biao:
            biao.add(word)


import socket, threading

class ClientThread(threading.Thread):
    
    def __init__(self,ip,port,clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.csocket = clientsocket
        print("[+] New thread started for "+ip+":"+str(port))
    
    
    def run(self):    
        print("Connection from : "+ip+":"+str(port))
        
        # clientsock.send(("\nWelcome to the server\n\n").encode())
        
        # data = "dummydata"
        
        # while len(data):
            # data = self.csocket.recv(2048)
            # print("Client(%s:%s) sent : %s"%(self.ip, str(self.port), data))
            # self.csocket.send("You sent me : "+data)
        data = str(self.csocket.recv(2048), encoding="utf8")
        print("client(%s:%s) sent : %s"%(self.ip, str(self.port), data))
        s = data
        l = len(s)
        v = [True]*l
        for ll in range(5):
            for i in range(l-ll):
                if v[i] and s[i:i+ll+1] in biao:
                    for j in range(i,i+ll+1):
                        v[j]=False
        res = ""
        for i in range(l):
            if v[i]:
                res += s[i]
            else:
                res += "*"
        self.csocket.send(bytes(res, encoding="utf8"))
        
        print("Client at "+self.ip+" disconnected...")
 
host = "127.0.0.1"
port = 9999

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.bind((host,port))

       

while True:
    tcpsock.listen(4)
    print("\nListening for incoming connections...")
    (clientsock, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsock)
    newthread.start()
 