import socket

if __name__ == '__main__':
    # 1.创建客户端连接套接字
    tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.和服务端套接字建立连接
    tcp_socket_client.connect(("192.168.103.167", 8080))
    # 3.传输数据
    tcp_socket_client.send("Hi~".encode(encoding="utf-8"))
    # 4.接收数据
    recv_data = tcp_socket_client.recv(1024)
    print(recv_data.decode(encoding="utf-8"))
    # 5.关闭连接
    tcp_socket_client.close()
