FROM python:3.9.18-alpine3.18

ADD countingbot.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV BOTTOKEN ""
ENV CHANNELID ""
ENV BOTID1 ""
ENV BOTID2 ""

CMD ["python", "./countingbot.py"]
