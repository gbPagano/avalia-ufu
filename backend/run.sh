#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 8000 
# alembic revision --autogenerate -m "First migration"
# (alembic upgrade head && alembic upgrade e0b3ac51a714)

# alembic upgrade head && alembic revision --autogenerate -m "Creating tables" && PGPASSWORD=postgres psql -h db -U postgres -d wikiprof -a -f /populate.sql 