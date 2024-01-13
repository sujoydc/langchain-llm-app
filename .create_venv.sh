#!/bin/bash
python3 -m venv $1
source $1/bin/activate
pip3 install --upgrade pip
cd $1
pip3 install -r requirements.txt
code .



