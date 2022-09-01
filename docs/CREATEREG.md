# Create a registry

>When using the ConnectIoT project you'll be required to create a registry for each group of devices you want to administrate.

---
## How to use this?
By importing the ConnectIoT class to your Python script you can create a registry using the create_registry method. You will have to get and validate the Near contract url, the Near account ID and the private key .

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.create_registry("new_registry_name")
```

---
## create_registry Method
|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry you want to create  |bool                                                                                                                                
```py
def create_registry(self, registry_name: str) -> bool:
        response = self.__call_method_api(
            'create_registry', {'registry_name': registry_name})
        if response.status_code != 200:
            return False
        return response.json()['data']
```