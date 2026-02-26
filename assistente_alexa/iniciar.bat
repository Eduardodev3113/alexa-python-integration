@echo off
echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Iniciando servidor Python...
start cmd /k python app.py

echo Iniciando ngrok...
start cmd /k ngrok http --domain=sippingly-scalene-abrielle.ngrok-free.dev 5000

echo Tudo rodando!
pause