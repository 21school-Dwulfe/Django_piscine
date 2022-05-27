#!/bin/bash

if [ "$(which python3)" ];
then

python3 --version

else
    #can work without quotes
    if [[ $(uname) == Darwin ]];
    then
        brew install python3
    elif [[ $(uname) == Linux ]];
    then
        sudo apt-get update && sudo apt-get install python3.9
    fi

fi

if [ "$(which pip)" ];
then
    echo pip is installed
    pip --version
else
    python -m ensurepip --upgrade
fi

if [ -d .venv ];
then
    rm -rf .venv
fi

# #setup env in local_lib
python3 -m venv .venv
# #activation
source .venv/bin/activate

python -m pip install --upgrade pip
sudo apt-get install python3
python -m pip install --upgrade --force-reinstall Django --target .venv
#python3 -m pip install --upgrade  --force-reinstall psycopg2-binary --target .venv
# django-admin startproject d04
# python manage.py startapp ex00
# python manage.py runserver
