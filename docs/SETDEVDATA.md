# Set data to a device

>When using the ConnectIoT project you'll have devices taking in data so with this method you will be able to register that data.
---
## How do I set data to a device?
By importing the ConnectIoT class to your Python script you can set data to an existing device using the set_device_data method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before setting data to a device make sure that the device exists.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.set_device_data('registry_name', 'device_name', {
                'value1': 1, 'value2': 3.5, 'value3': 'foobar'})
```

## set_device_data Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |bool        
|device_name : str |                The device you want to set data to|
|data : str|The data you want to set to the device|

```py
def set_device_data(self,
                        registry_name: str,
                        device_name: str,
                        data: dict) -> bool:
        response = self.__call_method_api(
            'set_device_data', {
                'registry_name': registry_name,
                'device_name': device_name,
                'data': {str(key): str(value) for key, value in data.items()}
            })
        if response.status_code != 200:
            return False
        return response.json()['data']
```