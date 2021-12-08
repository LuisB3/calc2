#FROM python:3.6-buster
#RUN apt-get update
#RUN adduser myuser
#USER myuser
#WORKDIR /home/myuser
#ENV PATH="/home/myuser/.local/bin:${PATH}"
#COPY --chown=myuser:myuser . .
#RUN pip install --upgrade pip setuptools wheel

#FROM python:3.6-buster
#RUN apt-get update
#RUN adduser myuser
#USER myuser
#WORKDIR /home/myuser
#ENV PATH="/home/myuser/.local/bin:${PATH}"
#COPY --chown=myuser:myuser . .
#RUN pip install -r requirements.txt

FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
