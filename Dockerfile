# Based on https://github.com/ikatson/docker-reviewboard

FROM python:2.7-slim

EXPOSE 8000

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
        build-essential python-dev libffi-dev libssl-dev patch \
        python-pip python-setuptools python-wheel python-virtualenv \
        uwsgi uwsgi-plugin-python \
        postgresql-client \
        python-psycopg2 python-ldap \
        default-libmysqlclient-dev default-mysql-client \
        git-core mercurial subversion python-svn && \
        rm -rf /var/lib/apt/lists/*

RUN mkdir /app
ADD . /app
ADD docker-files/start.sh /start.sh
ADD docker-files/uwsgi.ini /uwsgi.ini
ADD docker-files/shell.sh /shell.sh
ADD docker-files/upgrade-site.py /upgrade-site.py
ADD docker-files/python.wsgi /python.wsgi

RUN chmod +x /start.sh /shell.sh /upgrade-site.py

WORKDIR /app
#RUN ./setup.py install
RUN pip install -e .

WORKDIR /app/anytask_sync_extension
RUN pip install -e .

RUN pip install mysqlclient==1.4.6
RUN pip install requests

RUN ln -fs /usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata.py /usr/lib/python2.7/
RUN ln -fs /usr/lib/python2.7/plat-x86_64-linux-gnu/_sysconfigdata_nd.py /usr/lib/python2.7/

WORKDIR /
CMD /start.sh
