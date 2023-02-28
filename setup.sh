#!/bin/bash

DIR="venv"
 
if [ ! -d "$DIR" ] 
then
  echo "venv file is not present"
  echo "creating venv file"
  python3 -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
  pytest -vs --html=index.html --self-contained-html --md-report
  python3 app.py

else

  echo "present"
  source ./venv/bin/activate
  pytest -vs --html=index.html --self-contained-html --md-report
  python3 app.py

fi
