#!/usr/bin/python
import os

def vagrant():
    iniciar = "vagrant up"
    print(iniciar)

vagrant()

#instalação do Java

os.system('sudo apt-get install java-11-openjdk-devel')
os.system('sudo apt-get install java-11-openjdk')
os.system('sudo wget https://download.oracle.com/java/18/latest/jdk-18_linux-aarch64_bin.rpm')
os.system('sudo localinstall jre-18-linux-x64.rpm')
os.system('java -version')

#instalação do Zeppelin

os.system('wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')
os.system('sudo tar xf zeppelin-0.10.1-bin-all.tgz -C /opt')
os.system('sudo mv /opt/zeppelin-0.10.1-bin-all /opt/zeppelin')
os.system('sudo systemctl start zeppelin')
os.system('sudo systemctl enable zeppelin')

#Adicionar usuários
os.system('sudo cp conf/shiro.ini.template conf/shiro.ini')
os.system('sudo vim conf/shiro.ini')
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



