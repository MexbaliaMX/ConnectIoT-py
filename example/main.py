import os
from ConnectIoT import ConnectIoT

if __name__ == '__main__':
    contract = ConnectIoT(os.environ.get('NEAR_CONTRACT_URL'),
                          os.environ.get('NEAR_ACCOUNT_ID'),
                          os.environ.get('NEAR_PRIVATE_KEY'))
    registry_name = 'my_new_registry'
    device_name = 'my_new_device'
    if contract.create_registry(registry_name):
        new_device = contract.add_device_to_registry(
            registry_name, device_name, 'Device for python lib test.')
        if new_device:
            contract.set_device_data(registry_name, device_name, {
                'value1': 1, 'value2': 3.5, 'value3': 'foobar'})
            print(contract.get_device_data(registry_name, device_name))
    if contract.delete_device_from_registry(registry_name, device_name):
        contract.delete_registry(registry_name)
        print('Cleaned up')
