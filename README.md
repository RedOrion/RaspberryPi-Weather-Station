# RaspberryPi-Weather-Station

## Install
```shell
sudo mkdir /data
cd /data
git clone git@github.com:RedOrion/RaspberryPi-Weather-Station.git
```

## Initial Setup

Install the mysql server and client and setup the users for mysql

```bash
cd /data/RaspberryPi-Weather-Station/setup/
./packages.sh
./sql.sh
```

## Temperature cron
Get temperature at specified intervals
`0,15,30,45 * * * * /disk1/RaspberryPi-Weather-Station/server/temperature.py`
Pull updates
`5 7-20 * * * /data/RaspberryPi-Weather-Station/server/Update.sh`