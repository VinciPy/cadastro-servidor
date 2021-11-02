#!bin/bash
sudo apt update
sudo apt install iptables nginx-full rsync  iptables  mariadb-server #instalando webserver, firewall, mariadb, 
#instalando firebird
yes| sudo add-apt-repository ppa:mapopa/firebird3.0
sudoapt update
sudo apt-get install firebird3.0-server
sudo apt install -y python3.9 python3-pip
pip3 install django
django-admin startproject mysite
cd mysite
python3 manage.py runserver 0.0.0.0:8080


