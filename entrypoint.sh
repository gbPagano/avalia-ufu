#!/bin/bash

# Start your FastAPI application
uvicorn backend.main:app --host 0.0.0.0 --port 8000

sleep 10

# Execute the populate.sql script
psql -U postgres -d wikiprof -a -f /wikiprof/backend/populate.sql