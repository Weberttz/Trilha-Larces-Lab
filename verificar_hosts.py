import argparse, json, csv
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

def banner_grab(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    resultado = sock.connect_ex((host, porta))

    if resultado != 0: # se não conseguiu conectar
        return None
    
    portas_http = [80, 8080, 8000, 3000]

    if porta in portas_http: # percorre portas que precisam de request http
            sock.send("GET / HTTP/1.1\r\nHost: host\r\n\r\n".encode()) # envia os bytes 

    dados = sock.recv(1024) # recebe os bytes
    banner = dados.decode(errors="ignore") # transforma os bytes em string

    sock.close()
    return banner

def recolher_lista_hosts(caminho): # recebe um caminho para o aquivo
    hosts = []
    with open(caminho, "r") as f: # abre e pega todas as strings de hosts do arquivo
        host = f.read().replace('\n', '')
        hosts.append(host)

    return hosts

def salvar_json(resultados, arquivo): # salvar em json
    with open(arquivo, "w") as f: # abrir o arquivo e formatar com ident 4
        json.dump(resultados, f, indent=4)

def salvar_csv(resultados, arquivo): # salvar em csv
    with open("resultado.csv", "w", newline="") as arquivo: # abrir arquivo
        writer = csv.writer(arquivo) # criar um escritor
        
        # escreve cabeçalho
        writer.writerow(["porta", "status", "banner"])
        
        # escreve cada linha formatada
        for linha in resultados:
            writer.writerow([linha["porta"], linha["status"], linha["banner"]])

def imprimir_no_terminal(resultados): # imprimir todos os resultados direto no terminal
    for resultado in resultados:
       print(f"Porta: {resultado['porta']} | Status: {resultado['status']} | Banner: {resultado['banner']}")

def main():
    args = parse_args() # receber os argumentos via linha de comando
    portas_comuns = [21, 22, 80, 443, 3000, 8000, 8080] # portas com seviços comuns 
    resultados = []
    lista_hosts = recolher_lista_hosts(caminho=args.arquivo) # recolhe do arquivo e joga na lista de hosts

    # percorre lista de hosts e as portas comuns, tenando abrir conexão para cada porta em cada host
    for host in lista_hosts:  
        for porta in portas_comuns: 
            if scan_porta(host, porta):
                banner = banner_grab(host, porta)
                resultados.append({
                    "porta": porta,
                    "status": "aberta",
                    "banner": banner
                })

    if args.output == "json":
        salvar_json(resultados, "resultado.json")
    if args.output == "csv":
        salvar_csv(resultados, "resultado.csv")
    if args.output == "print":
        imprimir_no_terminal(resultados)

    
if __name__ == "__main__":
    main()