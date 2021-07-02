import socket

if __name__ == '__main__' :
    # 1.创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.连接绑定
    tcp_socket_server.bind(("192.168.103.167", 8888))
    # 3.监听请求
    tcp_socket_server.listen(128)
    # 4.等待连接请求
    # 5.接收数据
    # 6.传输数据
    # 7.关闭套接字