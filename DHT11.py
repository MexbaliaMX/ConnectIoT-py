
import datetime
import time
import Adafruit_DHT
from Adafruit_DHT.common import DHT11
import os
from ConnectIoT import ConnectIoT



dht11 = Adafruit_DHT.DHT11
# DHT sensor
# connected to GPIO17.
pinDHT11 = 17



if __name__ == '__main__':

        contract = ConnectIoT(
                          os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))
        print('API URL: '+contract.contract_api_url)

        registry_name = 'RaspberryPi2B'
        device_name = 'DHT11.0'

        print("Registry: "+registry_name)
        print("Device: "+device_name+" connected")
        bday= datetime.date.today()
        loc= '''19° 25' 42" N'''
        ps='9V'
        if contract.get_device_metadata(registry_name,device_name) == {}:
            contract.set_device_metadata(registry_name,device_name,
            {'Creation Date': bday, 'Location': loc, 'Power Supply': ps})
            print(contract.get_device_metadata(registry_name,device_name))
        else :

            print(contract.get_device_metadata(registry_name,device_name))
while True:
        today = datetime.date.today()
        timenow  = datetime.datetime.now().time().replace(microsecond=0)
        humidity, temperature = Adafruit_DHT.read_retry(dht11, pinDHT11)
        if humidity is not None and temperature is not None:
            print('Temperature={0:0.1f}°C Humidity={1:0.1f}%'.format(temperature, humidity))

            contract.set_device_data(registry_name, device_name,
            {'Date': today,
             'Temperature ': str(temperature)+' °C',
             'Datetime': timenow,
             'Humidity ': str(humidity)+' %',})
            print(contract.get_device_data(registry_name, device_name))

        else:
            print('Failed to get reading. Try again!')

            break
        time.sleep(50)
