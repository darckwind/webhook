#!/bin/bash

echo instalando entorno de para servidor de repicacion 
echo instalando pip

sudo yum install epel-release 
sudo yum install python-pip

echo instalando bibliotecas

/usr/bin/pip install flask
/usr/bin/pip install gitpython

echo instalando ngrok

sudo mkdir ngrok
cd ngrok/
wget -c https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip
echo ngrok instalado

