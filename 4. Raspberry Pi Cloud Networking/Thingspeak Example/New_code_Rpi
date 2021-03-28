import httplib, urllib  
import time  
import Adafruit_DHT
sleep = 2 # how many seconds to sleep between posts to the channel  
key = 'D2FFJV6KNJHV9UQG'  # Write API key 
  
humidity, temperature = Adafruit_DHT.read_retry(11, 4)  # GPIO27 (BCM notation)  
  
  
#Report Raspberry Pi internal temperature to Thingspeak Channel  
def thermometer():  
    while True:        
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}  
        conn = httplib.HTTPConnection("api.thingspeak.com:80")  
        try:  
            params = urllib.urlencode({'field1': temperature, 'key':key }) # channel name is field1 or field 2
            conn.request("POST", "/update", params, headers)  
            response = conn.getresponse()  
            print (humidity)  
            print (temperature)  
            #print response.status, response.reason  
            data = response.read()  
            conn.close()  
        except:  
            print ("connection failed")  
        break  
#sleep for desired amount of time  
if __name__ == "__main__":  
        while True:  
                thermometer()  
                time.sleep(sleep)  
                  
