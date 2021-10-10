FROM centos/python-38-centos7
MAINTAINER newcentury99

USER root
WORKDIR /app
COPY ./backend /app
COPY ./cmd.sh /

RUN pip install uWSGI==2.0.19.1
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["/cmd.sh"]
