#!/bin/sh
flask db upgrade # upgrade database

# Prepare log files and start outputting logs to stdout
mkdir -p /app/logs/
touch /app/logs/gunicorn.log
touch /app/logs/access.log
touch /app/logs/error.log

tail -n 0 -f /app/logs/*.log &

echo "Starting Gunicorn"

# Settings will be read from gunicorn.conf.py 
exec gunicorn \
    --access-logfile=/app/logs/access.log\
    --log-file=/app/logs/gunicorn.log\
    --error-logfile=/app/logs/error.log\
    --name=HealthTools_ZA\
    ${HEALTH_TOOLS_GUNICORN_EXTRA_CONFIG:-}

