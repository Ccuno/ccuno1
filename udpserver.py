import socket

def udp_server(server_ip, server_port, save_path):
    # 创建 UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定服务器地址
    server_socket.bind((server_ip, server_port))
    print(f"Server listening on {server_ip}:{server_port}")

    try:
        # 接收文件数据
        data, client_address = server_socket.recvfrom(4096)

        # 保存文件
        with open(save_path, 'wb') as file:
            file.write(data)

        print(f"File received and saved as '{save_path}' from {client_address}")

    except FileNotFoundError:
        print(f"Error: Save path '{save_path}' not found.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # 关闭 socket 连接
        server_socket.close()

if __name__ == "__main__":
    try:
        # 从命令行获取服务器 IP、端口和保存文件路径
        server_ip = input("Enter server IP: ")
        server_port = int(input("Enter server port: "))
        save_path = input("Enter save path for received file: ")

        # 启动 UDP 服务器
        udp_server(server_ip, server_port, save_path)

    except ValueError:
        print("Error: Invalid port number. Please enter a valid integer port.")

    except Exception as e:
        print(f"Unexpected error: {e}")

#运行环境： 代码可以在支持 Python 的任何环境中运行，例如 Python 3.x 版本。确保网络连接正常，以便在客户端和服务器之间进行通信。
#配置环境： 无需特殊配置。确保客户端和服务器能够相互访问，并且防火墙设置允许通过指定的端口进行通信。
#运行流程： 用户首先运行服务器端（udpserver.py），然后运行客户端端（udpclient.py）。客户端将要发送的文件路径、服务器 IP 和端口输入到命令行。服务器端监听指定端口，等待接收文件。客户端读取文件并通过 UDP 发送给服务器。服务器接收文件并保存到指定路径。