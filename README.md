# RSS2toot

A simple script that transport dynamic from RSS to Mastodon. 

一个将RSS动态搬运到长毛象的脚本。




```
pip3 install -r requirements.txt
cp conf.sample.ini conf.ini
nano conf.ini
python3 run.py
```

crontab job setting:
```
crontab -e
```
or (Ubuntu 18.04)
```
nano /etc/crontab
/etc/init.d/cron restart
```

Recommand do job hourly:
```
#m h dom mon dow user  command
13 *    * * *   root    cd /RSS2toot && python3 run.py
```
