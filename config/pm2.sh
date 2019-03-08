#!/bin/sh
gunicorn -c config/config_production.py api:app