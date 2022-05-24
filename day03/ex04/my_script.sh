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

if [ -d django_venv ];
then
    rm -rf django_venv
fi

# #setup env in local_lib
python3 -m venv django_venv
# #activation
source django_venv/bin/activate

python -m pip install --upgrade pip 
python -m pip install --upgrade --force-reinstall Django --target django_venv
python3 -m pip install --upgrade  --force-reinstall psycopg2-binary --target django_venv

