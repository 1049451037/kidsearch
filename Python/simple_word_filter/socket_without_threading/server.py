#-*- coding: utf-8 -*-
import socket  # 导入socket模块

biao = set()
with open("keywords", "r", encoding="utf-8") as f:
    for line in f.readlines():
        word = line.replace("\n", "")
        if word not in biao:
            biao.add(word)

while True:
    sk = socket.socket()  # 创建socket对象
    sk.bind(("127.0.0.1", 8888))  # 绑定端口,“127.0.0.1”代表本机地址，8888为设置链接的端口地址
    sk.listen(5)  # 设置监听，最多可有5个客户端进行排队
    conn, addr = sk.accept()  # 阻塞状态，被动等待客户端的连接
    print(conn)  # conn可以理解客户端的socket对象
    # <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9005), raddr=('127.0.0.1', 36694)>
    print(addr)  # addr为客户端的端口地址
    # ('127.0.0.1', 40966)
    accept_data = conn.recv(1024)  # conn.recv()接收客户端的内容，接收到的是bytes类型数据，
    accept_data2 = str(accept_data, encoding="utf8")  # str(data,encoding="utf8")用“utf8”进行解码
    print("".join(("接收内容：", accept_data2, "    客户端口：", str(addr[1]))))
    s = accept_data2
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
    send_data = res
    conn.sendall(bytes(send_data, encoding="utf8"))  # 发送内容必须为bytes类型数据，bytes(data, encoding="utf8")用“utf8”格式进行编码
    conn.close()