#!/bin/bash
docker compose down -v 
docker image rm -f avalia-ufu-backend
cd .. 
sudo rm -rf wikiprof_bd