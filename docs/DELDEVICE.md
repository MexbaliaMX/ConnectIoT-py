# Delete a device from a registry

>When using the ConnectIoT project you'll probably have to delete certain devices from your registries.
---
## How do I delete a device from a registry?
By importing the ConnectIoT class to your Python script you can delete an existing device from a registry using the delete_device_from_registry method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before deleting a device make sure that both registry and device exist.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.delete_device_from_registry('registry_name', 'device_name'):
```
## delete_device_from_registry Method
|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that stores the device  |bool        
|device_name : str |                The name of the device you want to delete|

```py
def delete_device_from_registry(self,
                                    registry_name: str,
                                    device_name: str) -> bool:
        response = self.__call_method_api(
            'delete_device_from_registry', {
                'registry_name': registry_name,
                'device_name': device_name
            })
        if response.status_code != 200:
            return False
        return response.json()['data']
```
