# speedcheck
## Because @!$# you Spectrum!

Pretty much a project born of neccessity. I have a cable tech from Spectrum coming in two hours and I want to have data to prove to them that their network is broken. I doubt it will do much, but I wanted to learn SQA anyways.

Update: The cable tech from Spectrum is going to be at least an hour behind. Yay.

### Requirements
* PostgreSQL (Server and Client Libraries)
* Python 3.x (writen on a Python 3.9 install)

### Installation

Clone into a fresh virtualenv.

`pip3 install -r requirements.txt`

Edit config.py to match your database

Run `ST_DBCREATE=TRUE python3 speedcheck.py` to have it create the tables, then run `python3 speedcheck.py` to have it run the tests and toss the results into your database. I have mine hooked into a crontab for every five minutes.
