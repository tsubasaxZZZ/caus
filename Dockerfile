FROM python:3.5

ADD web-settings/maus /etc/nginx/sites-available/
ADD web-settings/supervisord-maus.conf /etc/supervisor/conf.d/
ADD . /caus

RUN set -x && \
    apt-get update && \
    apt-get -y install nginx supervisor && \
    ln -sf /etc/nginx/sites-available/maus /etc/nginx/sites-enabled/ && \
    cd /caus && \
    pip install -r ./requirements.txt && \
    mkdir /var/run/uwsgi /var/log/uwsgi && \
    chown www-data:www-data /var/run/uwsgi /var/log/uwsgi

EXPOSE 8080
CMD ["/usr/bin/supervisord"]

