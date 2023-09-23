#!/usr/bin/env bash

# exit on error
set -o errexit

# dependencies via pip
pip install -r dependencies.txt

# run migrations in case any migration hadn't been run yet
python manage.py migrate

