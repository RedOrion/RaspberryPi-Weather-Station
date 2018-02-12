# RaspberryPi-Weather-Station


## Configuring Server

### Install Required Packages
````shell
sudo apt-get install npm
sudo npm install -g pm2
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