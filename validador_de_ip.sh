#!/usr/bin/env bash

# valida se passou somente um argumento
[[ $# -ne 1 ]] && echo "Forneça um endereço ip" && exit 1

ip=$1

# regex para validar se o IPV4 é válido
# 250 - 255 ou 200 - 249 ou 100 - 199 ou 10 - 99 ou 0 - 9
octeto="(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])"

# junção de três octetos separados por pontos e um último sem pontuação ao fim
regex="^($octeto\.){3}$octeto$"

# validação se uma string combina com uma expressão regular
if [[ $ip =~ $regex ]]; then
    echo "IP válido: $ip"
else
    echo "IP inválido: $ip"
fi
