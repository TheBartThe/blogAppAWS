FROM python:latest

WORKDIR /opt/blog-server

COPY requirements.txt .

RUN pip install -r requirements.txt

# copy the correct python script to the current working directory
COPY . blog-app

EXPOSE 5000

# an entrypoint has been set here
# the Python binary is executed, with the correct script as an argument
ENTRYPOINT ["/usr/local/bin/python", "blog-app/app.py"]
