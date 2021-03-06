import threading
import time
import socket

BUFSIZ = 1024


class MysocketServer(threading.Thread):

    def __init__(self, serverAddr, serverPort, dllFunci):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = serverPort  # 设置端口
        self.socket.bind((host, port))
        self.dllFunc = dllFunci
        # try:
        # 服务器永远等待客户端的连接


    # except KeyboardInterrupt:
    #     self.tcp_server.server_close()  # 关闭服务器套接字
    #     print('\nClose')
    #     exit()
    def run(self):
        print("socket listening!!")
        self.socket.listen(5)
        while True:  # conn就是客户端链接过来而在服务端为期生成的一个链接实例
            conn, addr = self.socket.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
            print(conn, addr)
            while True:
                try:
                    # conn.send(b"aaaa")

                    data = conn.recv(8192)  # 接收数据
                    # print(f"socket receive={len(data)}")
                    dataLen = len(data)
                    if len(data) > 0:
                        # print(data)
                        self.dllFunc.inputBuff(data, dataLen)
                    else:
                        print("zero!!!!!!!!")
                    # # conn.send(data.upper())  # 然后再发送数据
                except ConnectionResetError as e:
                    print('关闭了正在占线的链接！')
                    break
            conn.close()
