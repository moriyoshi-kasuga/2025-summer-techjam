#!/usr/bin/env bash

PORT=${1:-6000}

echo "Starting the Flask application on port $PORT..."

gunicorn -w 4 'app:app' --bind "0.0.0.0:$PORT"
