# RaspberryPi-Weather-Station

## Install
```bash
sudo mkdir /disk1
cd /disk1
git clone git@github.com:RedOrion/RaspberryPi-Weather-Station.git
```

## Initial Setup

```bash
cd /disk1/RaspberryPi-Weather-Station/setup/
./packages.sh
./sql.sh
```
## Examples
sql.sh
./sql.sh -s mysql.local -h weatherstationpi.local

## Temperature cron
Get temperature at specified intervals
`0,15,30,45 * * * * /disk1/RaspberryPi-Weather-Station/server/temperature.py`
Pull updates
`5 7-20 * * * /disk1/RaspberryPi-Weather-Station/server/Update.sh`