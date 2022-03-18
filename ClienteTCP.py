import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso')

    host_target = input('Diginte o host ou ip a ser conectado: ')
    port_target = input('Digite a porta da conexão: ')

    try:
        s.connect((host_target, int(port_target)))
        print('Cliente TCP conectado com sucesso: ' + host_target + ' - ' + port_target)
        s.shutdown(2)
    except socket.error as e:
        print('Não foi possível conectar no host: ' + host_target)
        print('Erro: {}'.format(e))


if __name__ == "__main__":
    main()