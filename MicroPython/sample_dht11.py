from dht11 import *
from time import sleep
 
dht2 = DHT(18) #temperature and humidity sensor connect to D18 port
 
 
while True:  
    temp,humid = dht2.readTempHumid()#temp:  humid:
    print(temp)
    print(humid)
    sleep(0.5)
