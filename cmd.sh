#!/bin/bash
set -e
echo "Running Production Server"
echo "[ HyperTech99's Page ]"
exec uwsgi uwsgi.ini
fi
