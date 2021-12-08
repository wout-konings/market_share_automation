FROM python:3.7
COPY ./* ./
#RUN apt-get update && apt-get install -y \ 
    #cmake \
    #libffi-dev \
    #curl \
    #gcc \
    #musl-dev \
    #python3-dev \
    #libffi-dev \
#RUN pip3 install pip setuptools
#RUN wget `curl -s https://api.github.com/repos/snowflakedb/snowflake-connector-python/releases/latest | grep "tarball_url" | cut -d : -f 2,3 | tr -d \" \ | tr -d ,`
#RUN tar -xf v2.*
#RUN pip3 install cryptography
#RUN pip3 install ./snowflakedb-snowflake-connector-python-* --no-use-pep517
RUN pip install -r requirements.txt
CMD [ "python3", "./marketshare.py"]



#FROM python:3.9-alpine3.13
#RUN pip install -r requirements.txt
#CMD [ "python", "./write_sheets.py"]




#FROM python:3-alpine
#ENV PROJ_DIR="/app"
#ENV LOG_FILE="${PROJ_DIR}/app.log"
#ENV CRON_SPEC="* * * * *" 
#WORKDIR ${PROJ_DIR}
#COPY . ${PROJ_DIR}
#RUN pip install -r requirements.txt
#RUN echo "${CRON_SPEC} python ${PROJ_DIR}/write_sheets.py >> ${LOG_FILE} 2>&1" > ${PROJ_DIR}/crontab
#RUN touch ${LOG_FILE} # Needed for the tail
#RUN crontab ${PROJ_DIR}/crontab
#RUN crontab -l
#CMD crond  && tail -f ${LOG_FILE} #crond runs per default in the background



#FROM python:3.7
#RUN apt-get update && apt-get -y install cron vim
#COPY crontab /etc/cron.d/crontab
#COPY ./* ./
#RUN chmod 0644 /etc/cron.d/crontab
#RUN /usr/bin/crontab /etc/cron.d/crontab
# run crond as main process of container
#CMD ["cron", "-f"]


#RUN yum -y update && yum -y install gcc openssl-devel bzip2-devel libffi-devel wget make && yum clean all
#RUN cd /opt && wget --no-check-certificate https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz && tar xzf Python-3.8.3.tgz && cd Python-3.8*/ && ./configure --enable-optimizations && make altinstall && rm -rf /opt/Python* && mkdir /pyscripts
#RUN yum -y install epel-release && yum clean all
#RUN yum makecache
#RUN yum install python34-setuptools
#RUN easy_install-3.4 pip
#RUN pip install -r requirements.txt
#RUN crontab crontab
#CMD ["crond", "-f"]