FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /event_bot

COPY requirements.txt /event_bot/
COPY start.sh start.sh

RUN pip install -r requirements.txt
RUN chmod +x ./start.sh


COPY . /event_bot

CMD chmod +x ./start.sh ; ./start.sh
