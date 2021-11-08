#!bin/bash ---- CONFIGURAÇÃO
sudo apt update 
#inslando todos os softwares
sudo apt install iptables nginx-full rsync  iptables  mariadb-server #instalando webserver, firewall, mariadb, 
#instalando firebird
yes| sudo add-apt-repository ppa:mapopa/firebird3.0
sudoapt update
sudo apt-get install firebird3.0-server
#instalando o python --- APLICAÇÃO
sudo apt install -y python3.9 python3-pip
#instalando o django para rodar a aplicao web
pip3 install django
git clone https://github.com/VinciPy/cadastro-servidor.git
cd cadastro-servidor
python3 manage.py runserver 0.0.0.0:8080
#rodando as migraçoes do banco de dados
python3 manage.py migrate 
python3 manage.py migrate server 
cd ..
#instalando antivirus -- ANTIVIRUS --
sudo apt install -y clamav
sudo freshclam
echo "0 1 * * * clamscan -r /home > logs-clmav.txt" | tee -a /var/spool/cron/root
#configurando backup -- BACKUP --
echo "0 1 * * * rsync -av --backup --backup-dir=/root/ 192.168.254.5::www > logs_backup.txt" | tee -a /var/spool/cron/root


#configurando o iptables -- IPTABLES
# Setting default policies:
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Exceptions to default policy
iptables -A INPUT -p tcp --dport 80 -j ACCEPT       # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT      # HTTPS
iptables -A INPUT -p tcp --dport 22 -j ACCEPT      # HTTPS




