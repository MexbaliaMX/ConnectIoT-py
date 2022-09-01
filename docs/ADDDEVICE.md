# Add Device To Registry

>When using the ConnectIoT project you'll have to add devices to your registries.

---

## How do I add a device to a registry?
By importing the ConnectIoT class to your Python script you can add device to a registry using the add_device_to_registry method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before adding a device make sure that the registry exists.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get                        ('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

new_device = contract.add_device_to_registry(
            'registry_name', 'device_name', 'Device for python lib test.')
```
---
## add_device_to_registry Method
|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry that will store your device  |bool        
|device_name : str |                The name of the device you want to create|
|description : str|      The description you want to give to the device |                                                                              
```py
def add_device_to_registry(self,
                               registry_name: str,
                               device_name: str,
                               description: str) -> bool:
        response = self.__call_method_api(
            'add_device_to_registry', {
                'registry_name': registry_name,
                'device_name': device_name,
                'description': description
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

```