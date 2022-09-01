# Set a data parameter to a device

>When using the ConnectIoT project you'll have devices taking in data with specific parameters so with this method you will be able to register those parameters individualy.
---
## How do I set a data param with its value?
By importing the ConnectIoT class to your Python script you can set a single data parameter with its value to an existing device using the set_device_data_param method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before setting a data param to a device make sure that the device exists. Remeber that this method is only for single param/value setting.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.set_device_data_param('registry_name', 'device_name', 'my_param', 'my_value')

```
## set_device_data_param Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |bool        
|device_name : str |                The device you want to set data to|
|param : str| The key you want to set for the new param in the device data|
|value : str|The value you want to set for the new param in the device data|

```py
def set_device_data_param(self,
                              registry_name: str,
                              device_name: str,
                              param: str,
                              value: str) -> bool:
        response = self.__call_method_api(
            'set_device_data_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param,
                'value': value
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

```