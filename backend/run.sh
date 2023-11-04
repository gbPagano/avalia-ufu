#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 8000 &
sleep 3 
echo Populando o banco... 
alembic upgrade head && echo Banco populado com sucesso.

while true
do
    sleep 1
done
