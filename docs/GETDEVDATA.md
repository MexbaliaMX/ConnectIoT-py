# Get data from device

>When using the ConnectIoT project you'll have devices taking in data so with this method you will be able to get and see that data.
---
## How do I get data from a device?

By importing the ConnectIoT class to your Python script you can get data from an existing device using the get_device_data method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before getting data from a device make sure that the registry and device exist.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

print(contract.get_device_data('registry_name', 'device_name'))
```

## get_device_data Method

|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |Dict        
|device_name : str |                The name of the device you want to delete|

```py
def get_device_data(self,
                        registry_name: str,
                        device_name: str) -> dict:
        response = self.__call_method_api(
            'get_device_data', {
                'registry_name': registry_name,
                'device_name': device_name
            })
        if response.status_code != 200:
            return None
        return response.json()

```