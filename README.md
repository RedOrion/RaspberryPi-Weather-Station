# RaspberryPi-Weather-Station


## Configuring the Server to always run on boot

### Install Required Packages
````shell
sudo apt-get install npm
````

### Starting PM2 on Boot
````shell
pm2 startup
````

### Starting temperature script with PM2
````shell
pm2 start [Location of Repo]/RaspberryPi-Weather-Station/server/temperature.py
````

### Enable restarting of PM2 after rebooting
````shell
pm2 save
````

### Controlling your temperature.py and other scripts via PM2

#### Restarting temperature script
````shell
pm2 restart temperature
````
#### Stopping temperature script
````shell
pm2 stop temperature
````
#### Show the temperature script logs
````shell
pm2 logs temperature
````
#### Show the temperature script process information
````shell
pm2 show temperature
````

## Configuring automatic updates

### Use cron to pull updates from github and auto restart the scripts via PM2

#### Add to crontab
You can change the check interval to whatever you want. Currently it is set to run 30 minutes past the hour
````shell
30 *  *   *   * /home/pi/Developer/RaspberryPi-Weather-Station/server/Update.sh && pm2	restart	temperature
````