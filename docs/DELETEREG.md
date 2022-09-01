# Delete a registry

>When using the ConnectIoT project you'll probably need to delete an entire registry in the contract-

---
## How do I delete a registry?
By importing the ConnectIoT class to your Python script you can delete a registry using the delete_registry method. You will have to get and validate the Near contract url, the Near account ID and the private key. Before deleting make sure that the registry is empty, this means there are no devices registered.

```py
import os
from ConnectIoT import ConnectIoT

contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))

contract.delete_registry("registry_name")
```

---
## delete_registry Method
|Parameter                                     |Description|Method Return                                                        |                                                      
 ------------------------------------------ | ------ |--------------------------------------------------------------------------------------------------------------------------- |
| registry_name : str                  | The name of the registry you want to delete  |bool                                                                                                                                
```py
 def delete_registry(self, registry_name: str) -> bool:
        response = self.__call_method_api(
            'delete_registry', {'registry_name': registry_name})
        if response.status_code != 200:
            return False
        return response.json()['data']
```