#!/usr/bin/env bash
set -e

venv=test_venv

echo "Create virtualenv"; echo
if [[ -d "$venv" ]]; then
   echo "virtual environment already exists, going to remove"
   rm -rf "$venv"
fi

/usr/bin/virtualenv "$venv"

echo "Install python packages"; echo
source "$venv/bin/activate"
pip install -r requirements.txt

echo "Setup virtualenv done"
