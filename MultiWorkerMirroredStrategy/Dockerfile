FROM continuumio/anaconda3

RUN apt-get update && apt-get install -y libgtk2.0-dev && \
    rm -rf /var/lib/apt/lists/*
RUN /opt/conda/bin/conda update --all --yes
RUN /opt/conda/bin/conda update -n base -c defaults conda
RUN /opt/conda/bin/conda config --set ssl_verify no
RUN /opt/conda/bin/conda install -c conda-forge tensorflow -y
RUN /opt/conda/bin/conda upgrade dask

WORKDIR /app
COPY main.py .
COPY mnist_setup.py .
ENTRYPOINT ["python", "/app/main.py"]