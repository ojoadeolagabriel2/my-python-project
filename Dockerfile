FROM python:3.8

ADD main.py /

COPY requirements.txt requirements.txt

RUN ls && pip install -r ./requirements.txt

EXPOSE 12345

CMD [ "./main.py" ]

ENTRYPOINT [ "python" ]