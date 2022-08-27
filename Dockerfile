FROM python:3.9.6

WORKDIR /logobot
COPY . /logobot
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "logobot"]
