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
        sudo apt-get update && sudo apt-get install python3.8
    fi

fi

if [ "$(which pip)" ];
then
    echo pip is installed
    pip --version
else
    python -m ensurepip --upgrade
fi

if [ -d local_lib ];
then
    rm -rf local_lib
fi

# #setup env in local_lib
python3 -m venv local_lib
# #activation
source local_lib/bin/activate

pip install --upgrade --log install.log --force-reinstall git+https://github.com/jaraco/path.git --target local_lib

python my_program.py
