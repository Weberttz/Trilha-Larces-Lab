# Trilha-Larces-Lab

Este diretório reúne os principais arquivos de automação e suporte do projeto. Aqui ficam scripts utilizados para validar redes, verificar conectividade e analisar registros de sistemas.

## Visão geral

O objetivo deste espaço é manter ferramentas práticas para tarefas de infraestrutura e diagnóstico, especialmente relacionadas a:

- validação de endereços IP;
- verificação de hosts e conectividade;
- varredura e análise de arquivos de log.

## Arquivos do diretório
- `coletar_informacoes.sh`  
  Script em Bash responsável coletar informações da máquina, como data, usuário, hostname, pid e versão do kernel e criar um arquivo de relatório com esses dados.

- `validador_de_ip.sh`  
  Script em Bash responsável por validar endereços IP. Ele verifica se um valor informado está em um formato válido, como IPv4, e identifica entradas incorretas.

- `varredor-de-logs.sh`  
  Script em Bash que percorre arquivos de log em busca de padrões, erros, falhas e eventos relevantes. É útil para diagnóstico rápido de problemas em sistemas e serviços.

- `verificar_hosts.py`  
  Script em Python para checar se determinados hosts ou endereços estão acessíveis. Ele pode ser usado para testar disponibilidade e monitorar serviços ativos.

## Como esse diretório é usado

Esse espaço funciona como uma área de ferramentas úteis para administração e suporte técnico. Em vez de armazenar código de aplicação mais complexo, ele reúne utilitários que ajudam a:

- confirmar se um IP está correto;
- localizar erros em arquivos de log;
- verificar se um host está respondendo corretamente.

## Como executar os scripts
Para executar o script `coletar_informacoes.sh`, basta passar o nome do script como primeito argumento
```bash
bash coletar_informacoes.sh
```

Para executar o script `validador_de_ip.sh`, basta passar o nome do script como primeiro argumento e o ip que deseja valida como segundo argumento. Por exemplo:
```bash
bash validador_de_ip.sh <ip>
```

Para executar o script `varredor_de_logs.sh`, basta passar o nome do script como primeito argumento e o diretório onde deseja ler os arquivos com extensão .log. 
```bash
bash varredor_de_logs.sh <diretório>
```

Para executar o script `verificar_hosts.py`, você deve passar o arquivo com os hosts, e o formato de saída. Por exemplo:
```bash
python3 verificar_hosts.py --arquivo hosts.txt --output json
```