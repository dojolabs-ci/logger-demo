FROM python:2.7-slim-stretch
RUN apt-get update && apt-get -y install vim less
COPY app /usr/local/
RUN pip install -r /usr/local/requirements.txt
RUN mkdir -p /var/log/dojo/
#CMD python /usr/local/app.py &> /var/log/dojo/app.log
CMD [ "python", "/usr/local/app.py" ]
