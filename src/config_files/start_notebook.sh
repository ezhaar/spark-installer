#!/bin/bash

NBFILE="/home/ubuntu/nbserver.pem"
if [ ! -f $NBFILE ];
then
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -subj "/C=US/ST=Izhar/L=Stockholm/O=Dis/CN=www.example.com" \
    -keyout /home/ubuntu/nbserver.pem \
    -out /home/ubuntu/nbserver.pem
fi

PASSWD_FILE=/home/ubuntu/.ipython/profile_nbserver/nbpasswd.txt

if [ ! -f $PASSWD_FILE ];
 then
     python -c "from IPython.lib import passwd; print passwd()" > $PASSWD_FILE
fi

cd /home/ubuntu/notebooks
ipython notebook --profile=nbserver

