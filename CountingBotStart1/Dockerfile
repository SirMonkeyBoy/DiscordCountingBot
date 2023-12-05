FROM python:3.9.18-alpine3.18

ADD startcommand.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV COUNTSTARTNUMBER "1"
ENV BOTTOKEN ""

CMD [ "python", "./startcommand.py" ]