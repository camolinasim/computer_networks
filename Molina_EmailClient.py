#!/usr/bin/env python3

import socket

HOST = 'smtp.utep.edu'  # The server's hostname or IP address
PORT = 25               # The port used by the server


# sends message to server over a socket connection
def send_and_print(socket, msg):
    s.send(msg)
    data = s.recv(1024)
    print('Received', repr(data))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connecting to server
    s.connect((HOST, PORT))

    # Sending helo comand
    send_and_print(s, b'HELO \r\n')

    # Sending mail from command
    send_and_print(s, b'mail from: <camolinasim@miners.utep.edu>\r\n')

    # Sending rcpt to command
    send_and_print(s, b'rcpt to: <camolinasim@miners.utep.edu>\r\n')

    # Sending data command
    send_and_print(s, b'data\r\n')

    # Sending subject command
    send_and_print(s, b'subject: smpt_lab \r\n\r\n')

    # Sending body
    s.send(b'This lab works!! :)\r\n')

    # Ending body
    send_and_print(s, b'.\r\n\r\n')
