# magpi_downloader
Downloads all issues of MagPi in parallel

# Summary
The python script is solely responsible for scraping the proper .pdf
urls from the magpi website.  This data is then piped into xargs and
wget in order to download the magazines in parallel and save the files

```
cd magpi_downloader
mkdir magazines
virtualenv venv
source venv/bin/activate
pip install -r pip.install.lock

python magpi_downloader.py | xargs -n1 -P10 -I% sh -c 'result=`echo % | rev | cut -d"/" -f1 | rev` && wget -c % -O magazines/$result'
```
