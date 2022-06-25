#!/usr/bin/python

import os

#Instalação do Python 3.6

os.system('sudo apt-get install -y python36u python36u-libs python36u-devel python36u-pip')
os.system('python3.6 -V')

#Instalação do Apache Superset

os.system('sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-pip libsas12-dev libldap2-dev')
os.system('pip install --upgrade setuptools pip')
os.system('pip install superset') #instalar o superset
os.system('fabmanager create-admin --app superset') #criar o usuário admin
os.system('superset load_examples') #gerar dados
os.system('superset db upgrade') #inicializar o banco de dados
os.system('superset init') #iniciar o superset
os.system('superset run -h 0.0.0.0 -p 8088 --with-threads --debugger --reload') #rodar o webserver

#Instalação do MySQL
os.system('pip install mysqlclient') #instalar
#realizar a integração ao subir o superset

#Instalação do redis
os.system('pip install redis') #instalar
#realizar a integração ao subir o superset
