#!/usr/bin/env bash

[[ $# -ne 1 ]] && echo "Forneça um nome para diretório" && exit 1

# se existir, sai do scrip
[[ -d "$1" ]] && echo "Diretório já existe" && exit 1

diretorio=$1

echo "Criando um diretório..."
mkdir $diretorio

echo "Entrando no diretório..."
cd $diretorio

echo "Mostrando a localização do diretório..."
pwd 

echo "Criando dois arquivos no diretório..."

for n in 1 2 3 4; do
    touch arquivo$n.txt
done

echo "Lendo o que possui no diretório..."
ls -la

echo "Executando: 'echo Weberttz >> arquivo1.txt'"
echo "Weberttz" >> arquivo1.txt

echo "Lendo arquivo do diretório..."
cat arquivo1.txt

echo "Adeus!!!"

echo "Saindo do diretório, e apagando-o"
cd ..

rm -r $diretorio

echo "Remoção concluída!!!"