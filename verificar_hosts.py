import argparse
import socket

def parse_args(): # arg parse para rodar por linha de comando
    parser = argparse.ArgumentParser(description="Passe os argumentos!")
    parser.add_argument("--arquivo", help="Arquivo com hosts", required=True)
    parser.add_argument("--output", choices=["json", "csv", "print"], default="print")
    
    return parser.parse_args()

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket Ipv4 + TCP
    sock.settimeout(1) # tempo de um segundo
    resultado = sock.connect_ex((host, porta)) # tenta abrir conexão
    sock.close() # fecha socket
    return resultado == 0

def recolher_lista(caminho): # recebe um caminho para o aquivo
    hosts = []
    with open(caminho, "r") as f: # abre e pega todas as strings de hosts do arquivo
        host = f.read().replace('\n', '')
        hosts.append(host)

    return hosts

def main():
    args = parse_args() # receber os argumentos via linha de comando
    portas_comuns = [21, 22, 80, 443, 3000, 8000, 8080] # portas com seviços comuns 

    lista_hosts = recolher_lista(caminho=args.arquivo) # recolhe do arquivo e joga na lista de hosts

    # percorre lista de hosts e as portas comuns, tenando abrir conexão para cada porta em cada host
    for host in lista_hosts:  
        for porta in portas_comuns: 
            resultado = scan_porta(host, porta)

            if resultado: # se o resultado for diferente de 0, então o host responde
                print(f"Host: {host} responde na porta {porta}!")

if __name__ == "__main__":
    main()