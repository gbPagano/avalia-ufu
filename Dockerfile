# FROM postgres
# ENV POSTGRES_USER postgres
# ENV POSTGRES_PASSWORD postgres
# ENV POSTGRES_DB wikiprof
# COPY ./backend/populate.sql /docker-entrypoint-initdb.d

FROM python:3.11
WORKDIR /wikiprof
COPY ./requirements.txt /wikiprof/requirements.txt
COPY ./backend/ /wikiprof/backend/
COPY ./frontend/ /wikiprof/frontend/
COPY ./entrypoint.sh /wikiprof/
RUN chmod +x /wikiprof/entrypoint.sh
RUN pip install --no-cache-dir --upgrade -r /wikiprof/requirements.txt
CMD ["/wikiprof/entrypoint.sh"]

# FROM node:18.17.0
# WORKDIR /wikiprof/frontend
# RUN npm install
# RUN npm start