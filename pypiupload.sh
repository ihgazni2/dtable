#!/bin/bash
rm -rf dist
python3 setup.py sdist
set -x
XYZ=$(expect -c "
    spawn twine upload dist/*
    expect \"Enter your username: \"
    send \"${1}\r\"
    expect \"Enter your password: \"
    send \"${2}\r\"
    expect \"${PWD}\"
    send \"ls -l\r\"
")

