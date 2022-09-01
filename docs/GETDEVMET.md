# Get metadata from a device

>When using the ConnectIoT project you'll have devices taking in metadata so with this method you will be able to get and see that metadata.
---
## How do I get a device's metadata?

By importing the ConnectIoT class to your Python script you can get metadata from an existing device using the get_device_data method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before getting metadata from a device make sure that the device exists.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

print(contract.get_device_metadata(registry_name, device_name))
```
## get_device_data Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |str        
|device_name : str |                The name of the device you want to delete|

```py
def get_device_metadata_param(self,
                                  registry_name: str,
                                  device_name: str,
                                  param: str) -> str:
        response = self.__call_method_api(
            'get_device_metadata_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param
            })
        if response.status_code != 200:
            return 'None'
        return response.json()['data']
```