FROM jenkins-ansible:latest

USER root

RUN apt-get -y install nginx openssl python3-venv

RUN pip3 install poetry --upgrade 

COPY pyproject.toml .

RUN poetry install

COPY  webapp /webapp

VOLUME /var/www/html /var/log/nginx

COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf

COPY ./bin/start.sh /start.sh

EXPOSE 80

RUN chmod +x /start.sh

CMD /start.sh
