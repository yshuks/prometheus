FROM python:slim

# name of developer
LABEL maintainer=rajat.rsigmoidanalytics.com

# This is to work in the directory.
WORKDIR /usr/local/src

# copy the requirement file to install the required packages. 
COPY ./src/requirements.txt .

# fire the run command to install the packages
RUN pip3 install -r requirements.txt

# copy the python code to run on container
COPY ./src/app.py .

# run the python command to execute the python code
CMD ["python" , "app.py"]
