# RaspberryPi-Weather-Station


## Configuring Server

### Install Required Packages
````shell
sudo apt-get install npm
sudo npm install -g pm2
````


### Configure pm2

pm2 startup
pm2 start [Location of Repo]/RaspberryPi-Weather-Station/server/temperature.py
pm2 save

### Controlling your temperature.py and other scripts via PM2

With your Temperature script running via PM2, you have some handy tools at hand:


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