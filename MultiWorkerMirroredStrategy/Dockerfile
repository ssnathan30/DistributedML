# Use the base image
FROM learn/basedtf:1.0.0

WORKDIR /app
COPY main.py .
COPY mnist_setup.py .

ENTRYPOINT ["python", "/app/main.py"]