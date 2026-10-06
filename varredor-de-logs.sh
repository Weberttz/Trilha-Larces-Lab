#!/usr/bin/env bash


# valida se a quantidade de argumentos passados é diferente de 1
# caso seja, sai do script
[[ $# -ne 1 ]] && echo "Passe um diretório como argumento" && exit 1

# valida se o diretório passado existe
[[ ! -d "$1" ]] && echo "Diretório não existe" && exit 1

# variável 
dir=$1

# impressão de título
echo "------------------ ARQUIVOS DE LOGS FICTÍCIOS ------------------"
echo ""

# percorre cada arquivo .log do diretório passado
for f in "$dir"/*.log; do
    # recolhe o tamanho (número de caracteres) do arquivo
    tamanho=$(wc -c < "$f")
    # recolhe nome do arquivo
    nome=$(basename "$f" < "$dir")
    # imprime nome e tamanho
    echo "O tamanho do arquivo $nome é $tamanho"
    # pega as últimas 3 do arquivo e imprime
    tail -3 "$f" 
   
    echo ""
    echo ""
done