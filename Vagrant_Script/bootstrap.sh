#!/bin/bash

sudo apt update
sudo apt install vagrant

vagrant init centos/7
vagrant plugin install vagrant-disksize

vagrant up
vagrant ssh