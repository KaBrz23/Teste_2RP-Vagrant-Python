#!/usr/bin/python

import os

#Instalação Java

os.system ('wget --no-cookies --no-check-certificate --header "Cookie:oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.rpm"')
os.system ('sudo yum -y localinstall jdk-8u151-linux-x64.rpm')
os.system('java -version')
os.system('readlink -f $(which java)')
os.system('echo "export JAVA_HOME=/usr/java/jdk1.8.0_151" >> ~/.bash_profile')
os.system('echo "export JRE_HOME=/usr/java/jdk1.8.0_151/jre" >> ~/.bash_profile')
os.system('source ~/.bash_profile')

#Instalação do Zeppelin

os.system('wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')
os.system('sudo tar xf zeppelin-*-bin-all.tgz -C /opt')
os.system('sudo mv /opt/zeppelin-*-bin-all /opt/zeppelin')
os.system('sudo systemctl start zeppelin')
os.system('sudo systemctl enable zeppelin')

#Adicionar usuários
os.system('sudo cp conf/shiro.ini.template conf/shiro.ini')
os.system('sudo nano conf/shiro.ini')
#Inserir na ferramenta de edição 
#[users]
#2rp-guilherme = ZCteAb0TMvQkg, admin
#2rp-rene = HJndjeSdjeinS, admin
#2rp-cristiano = fenwmiHDSsnDs, admin
#2rp-kevin = mDkfekxlDgeFj, user
#2rp-mario = ikDmklFklmFkI, user
#2rp-lucas = kNBIVuOygyHUg, user
#2rp-ioram = UgdbhDYGssgru, user
#2rp-matheus = fheuNDsjdheIS, user
os.system('sudo systemctl restart zeppelin')

#OU instale via docker

os.system('docker run -p 8888:8080 --rm --name zeppelin apache/zeppelin:0.10.1')

