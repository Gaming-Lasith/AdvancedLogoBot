FROM python:3.9.6

WORKDIR /logo
COPY . /logo
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "logo"]
