FROM python:3.11
WORKDIR /wikiprof
COPY ./backend/ /wikiprof/backend/
# RUN apt-get update
# RUN apt-get install -y postgresql-client
RUN chmod +x ./backend/run.sh
RUN pip install --no-cache-dir --upgrade -r /wikiprof/backend/requirements.txt
WORKDIR /wikiprof/backend
CMD ["./run.sh"]