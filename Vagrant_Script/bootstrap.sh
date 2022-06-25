#!/bin/bash

sudo apt-get update #Atualizações
sudo apt-get install vagrant #Instalação do Vagrant
sudo apt-get install virtualbox #Instalação do VirtualBox

mkdir vagrantfile #Criar o diretório do vagrant
cd vagrantfile #Mudar para o diretório

vagrant init centos/7 #Inicialização do vagrant
vagrant plugin install vagrant-disksize #Instalação de plugin

#Abrir o vagrantfile e adicionar os comandos de configuração
vim vagrantfile #após a configuração, salvar e sair com wq!

vagrant up #Criar o ambiente

vagrant ssh #acesso ssh