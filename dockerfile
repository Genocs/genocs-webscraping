FROM python:3.9.13

# http port exposed outside the container
EXPOSE 5400

# Set the Current Working Directory inside the container
WORKDIR /app

RUN apt-get update

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install requests
RUN pip install gevent

# Copy the source code into the container 
COPY ./src/ .

# Run the application
CMD ["python", "main.py"]