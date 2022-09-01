# Set metadata to a device

>When using the ConnectIoT project you'll want your devices to have certain metadata. With this method you can set metadata to a device.    
---
## How do I set metadata to a device?
By importing the ConnectIoT class to your Python script you can set metdata to an existing device using the set_device_metadata method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before setting metadata to a device make sure that the device exists.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.set_device_data(registry_name, device_name, {
                'date': '01/01/1999', 'battery': '88%', 'Mod': 'DHT11'})
```

## set_device_metadata Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |bool        
|device_name : str |                The device you want to set data to|
|metadata : str|The data you want to set to the device|

```py
def set_device_metadata(self,
                        registry_name: str,
                        device_name: str,
                        metadata: dict) -> bool:
        response = self.__call_method_api(
            'set_device_metadata', {
                'registry_name': registry_name,
                'device_name': device_name,
                'metadata': {str(key): str(value) for key, value in data.items()}
            })
        if response.status_code != 200:
            return False
        return response.json()['data']
```