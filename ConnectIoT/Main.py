import requests


class ConnectIoT:
    """ Contract constructor to interact with the ConnectIoT project.

    Parameters
    ----------
    contract_api_url : str
        The url for the [api](https://github.com/paul-cruz/ConnectIoT-API.git) that allows you to connect with a ConnectIoT contract for exapmle an ip with its port ip:port 
    near_account_id : str
        The id for your NEAR Wallet account, it could be [testnet](https://wallet.testnet.near.org/) or [mainnet](https://wallet.near.org/) according to your contract
    near_account_private_key : str
        Your account [private key](https://docs.near.org/concepts/basics/accounts/account-id) to authenticate in the blockchain
    """

    def __init__(self,
                 contract_api_url: str,
                 near_account_id: str,
                 near_account_private_key: str) -> None:
        self.contract_api_url = contract_api_url
        self.__near_account_id = near_account_id
        self.__near_account_private_key = near_account_private_key

    def __call_method_api(self, method_name: str, params: dict) -> requests.Response:
        payload = {
            'account_id': self.__near_account_id,
            'params': params,
            'method': method_name
        }

        return requests.post(
            'http://{}/call'.format(self.contract_api_url),
            json=payload,
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': 'Bearer {}'.format(self.__near_account_private_key)
            })

    def create_registry(self, registry_name: str) -> bool:
        """ Method to create a registry in the contract. It communicates with the [create_registry ConnectIoT](https://github.com/paul-cruz/Connect-IoT#create_registry) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry you want to create

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'create_registry', {'registry_name': registry_name})
        if response.status_code != 200:
            return False
        return response.json()['data']

    def delete_registry(self, registry_name: str) -> bool:
        """ Method to delete a registry in the contract. It communicates with the [delete_registry ConnectIoT](https://github.com/paul-cruz/Connect-IoT#delete_registry) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry you want to delete

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'delete_registry', {'registry_name': registry_name})
        if response.status_code != 200:
            return False
        return response.json()['data']

    def add_device_to_registry(self,
                               registry_name: str,
                               device_name: str,
                               description: str) -> bool:
        """ Method to add a device in a registry in the contract. It communicates with the [add_device_to_registry ConnectIoT](https://github.com/paul-cruz/Connect-IoT#add_device_to_registry) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that will store your device
        device_name : str
            The name of the device you want to create
        description : str
            The description you want to give to the device

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'add_device_to_registry', {
                'registry_name': registry_name,
                'device_name': device_name,
                'description': description
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

    def delete_device_from_registry(self,
                                    registry_name: str,
                                    device_name: str) -> bool:
        """ Method to delete a device in a registry in the contract. It communicates with the [delete_device_from_registry ConnectIoT](https://github.com/paul-cruz/Connect-IoT#delete_device_from_registry) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to delete

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'delete_device_from_registry', {
                'registry_name': registry_name,
                'device_name': device_name
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

    def set_device_data(self,
                        registry_name: str,
                        device_name: str,
                        data: dict) -> bool:
        """ Method to set data to a device in a registry in the contract. It communicates with the [set_device_data ConnectIoT](https://github.com/paul-cruz/Connect-IoT#set_device_data) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to update
        data : str
            The data you want to set to the device

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'set_device_data', {
                'registry_name': registry_name,
                'device_name': device_name,
                'data': {str(key): str(value) for key, value in data.items()}
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

    def get_device_data(self,
                        registry_name: str,
                        device_name: str) -> dict:
        """ Method to get data from a device in a registry in the contract. It communicates with the [get_device_data ConnectIoT](https://github.com/paul-cruz/Connect-IoT#get_device_data) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to get the data from

        Returns
        ----------
        dict
            Dict with the device data
        """
        response = self.__call_method_api(
            'get_device_data', {
                'registry_name': registry_name,
                'device_name': device_name
            })
        if response.status_code != 200:
            return None
        return response.json()

    def set_device_data_param(self,
                              registry_name: str,
                              device_name: str,
                              param: str,
                              value: str) -> bool:
        """ Method to set a single param with its value to the device data in a registry in the contract. It communicates with the [set_device_data_param ConnectIoT](https://github.com/paul-cruz/Connect-IoT#set_device_data_param) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to update
        param : str
            The key you want to set for the new param in the device data
        value : str
            The value you want to set for the new param in the device data

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
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

    def get_device_data_param(self,
                              registry_name: str,
                              device_name: str,
                              param: str) -> str:
        """ Method to get a single param value from the device data in a registry in the contract. It communicates with the [get_device_data_param ConnectIoT](https://github.com/paul-cruz/Connect-IoT#get_device_data_param) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to consult
        param : str
            The key you want to get from a device data param

        Returns
        ----------
        str
            The param value
        """
        response = self.__call_method_api(
            'get_device_data_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param
            })
        if response.status_code != 200:
            return 'None'
        return response.json()['data']

    def set_device_metadata(self,
                            registry_name: str,
                            device_name: str,
                            metadata: dict) -> bool:
        """ Method to set metadata to a device in a registry in the contract. It communicates with the [set_device_metadata ConnectIoT](https://github.com/paul-cruz/Connect-IoT#set_device_metadata) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to update
        metadata : str
            The metadata you want to set to the device

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'set_device_metadata', {
                'registry_name': registry_name,
                'device_name': device_name,
                'metadata': {str(key): str(value) for key, value in metadata.items()}
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

    def get_device_metadata(self,
                            registry_name: str,
                            device_name: str) -> dict:
        """ Method to get metadata from a device in a registry in the contract. It communicates with the [get_device_metadata ConnectIoT](https://github.com/paul-cruz/Connect-IoT#get_device_metadata) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to get the metadata from

        Returns
        ----------
        dict
            Dict with the device metadata
        """
        response = self.__call_method_api(
            'get_device_metadata', {
                'registry_name': registry_name,
                'device_name': device_name
            })
        if response.status_code != 200:
            return None
        return response.json()

    def set_device_metadata_param(self,
                                  registry_name: str,
                                  device_name: str,
                                  param: str,
                                  value: str) -> bool:
        """ Method to set a single param with its value to the device metadata in a registry in the contract. It communicates with the [set_device_metadata_param ConnectIoT](https://github.com/paul-cruz/Connect-IoT#set_device_metadata_param) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to update
        param : str
            The key you want to set for the new param in the device metadata
        value : str
            The value you want to set for the new param in the device metadata

        Returns
        ----------
        bool
            If the operation was successfully executed
        """
        response = self.__call_method_api(
            'set_device_metadata_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param,
                'value': value
            })
        if response.status_code != 200:
            return False
        return response.json()['data']

    def get_device_metadata_param(self,
                                  registry_name: str,
                                  device_name: str,
                                  param: str) -> str:
        """ Method to get a single param value from the device metadata in a registry in the contract. It communicates with the [get_device_metadata_param ConnectIoT](https://github.com/paul-cruz/Connect-IoT#get_device_metadata_param) function.

        Parameters
        ----------
        registry_name : str
            The name of the registry that stores your device
        device_name : str
            The name of the device you want to consult
        param : str
            The key you want to get from a device metadata param

        Returns
        ----------
        str
            The param value
        """
        response = self.__call_method_api(
            'get_device_metadata_param', {
                'registry_name': registry_name,
                'device_name': device_name,
                'param': param
            })
        if response.status_code != 200:
            return 'None'
        return response.json()['data']
