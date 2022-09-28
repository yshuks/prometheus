FROM python


WORKDIR /usr/local/source

COPY ./source/requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./source/app.py .

CMD ["python" , "app.py"]
