# Get a device data parameter value
>When using the ConnectIoT project you'll have devices taking in data parameters with values so with this method you will be able to get and see those parameters values individualy.
---
## How do I get a data parameter value?
By importing the ConnectIoT class to your Python script you can get a single data parameter value from an existing device using the get_device_data_param method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before getting a data param value from a device make sure that the device and the parameter exist. Remeber that this method is only for single param/value getting.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

print(contract.get_device_data_param('registry_name', 'device_name', 'my_param'))
```
## get_device_data_param Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |str        
|device_name : str |                The device you want to set data to|
|param : str| The key you want to get from a device data param|


```py
def get_device_data_param(self,
                              registry_name: str,
                              device_name: str,
                              param: str) -> str:
        response = self.__call_method_api(
            'get_device_data_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param
            })
        if response.status_code != 200:
            return 'None'
        return response.json()['data']
```