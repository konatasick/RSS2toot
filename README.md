# weixin2toot

A simple script that transport dynamic from Weixin to Mastodon. Based on the Weixin RSS feed powered by [RSSHub](https://rsshub.app/)(From CareerEngine).

一个将微信公众号动态搬运到长毛象的脚本——基于[RSShub](https://rsshub.app/)生成的微信公众号动态RSS（CareerEngine 来源）。




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
13 *    * * *   root    cd /bili2toot && python3 run.py
```
