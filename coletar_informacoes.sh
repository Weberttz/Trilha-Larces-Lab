#!/usr/bin/env bash

arquivo="relatorio_$(date +%F).txt"

{
    echo "CAMPO|VALOR"
    echo "Data|$(date)"
    echo "Usuário|$USER"
    echo "Hostname|$(hostname)"
    echo "PID|$$"
    echo "Kernel|$(uname -rms)"
} | column -t -s '|' > "$arquivo"

cat "$arquivo"