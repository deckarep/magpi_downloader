#!/usr/bin/env bash
python magpi_downloader.py | xargs -n1 -P10 -I% sh -c 'result=`echo % | rev | cut -d"/" -f1 | rev` && wget -c % -O magazines/$result'
