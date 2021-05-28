FROM python:3.8
WORKDIR /project
COPY ./ ./
RUN pip install -r ./requirements.txt
EXPOSE 12345
CMD [ "./main.py" ]
ENTRYPOINT [ "python" ]