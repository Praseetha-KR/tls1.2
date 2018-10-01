import socket
from consts import SERVER_NAME
from client_inputs import (
    client_hello, client_key_exchange, client_change_cipher_spec,
    client_encrypted_handshake_message
)
from formats import (
    server_hello_format, server_certificate_format, server_key_exchange_format,
    server_hello_done_format
)


try:
    ip = socket.gethostbyname(SERVER_NAME)
    print('IP: {}'.format(ip))
except socket.gaierror as err:
    print('Couldn\'t resolve host IP. {}'.format(err))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 443))
s.sendall(client_hello)
response = b''
while True:
    result = s.recv(1024)
    print('Recieved chunk of size {}...'.format(len(result)))
    response += result
    if not result:
        print('End of response.')
        break


offset = 0
server_hello = server_hello_format.parse(response)
server_hello_len = server_hello.record_length + 5
offset += server_hello_len
server_certificate = server_certificate_format.parse(response[offset:])
server_certificate_len = server_certificate.record_length + 5
offset += server_certificate_len
server_keyexchange = server_key_exchange_format.parse(response[offset:])
server_keyexchange_len = server_keyexchange.record_length + 5
offset += server_keyexchange_len
server_hello_done = server_hello_done_format.parse(response[offset:])

print('Server Hello: \n{}\n\n'.format(server_hello))
print('Server Certificate: \n{}\n\n'.format(server_certificate))
print('Server Key Exchange: \n{}\n\n'.format(server_keyexchange))
print('Server Hello Done: \n{}\n\n'.format(server_hello_done))

s.sendall(
    client_key_exchange +
    client_change_cipher_spec +
    client_encrypted_handshake_message
)
response = b''
while True:
    result = s.recv(1024)
    print('Recieved chunk of size {}...'.format(len(result)))
    response += result
    if not result:
        print('End of response.')
        break

s.close()
print(response)
