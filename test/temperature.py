#!/usr/bin/python3

#https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf

import os
import glob
import time
import sys, getopt

def main(argv):
    loop = False
    try:
        opts, args = getopt.getopt(argv,"lh")
    except getopt.GetoptError:
        print("arg failure")
    for opt, arg in opts:
        if opt == '-h':
            print("temperature.py -l (loop)")
            print("temperature.py (for default path)")
            sys.exit()
        if opt == '-l':
            loop = True

    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
    base_dir = '/sys/bus/w1/devices/'

    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
            
    if loop == False:
        print(read_temp())
    else:
        while True:
            print(read_temp())
            time.sleep(1)

if __name__ == "__main__":
   main(sys.argv[1:])