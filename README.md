# Python Kerberos Vault Integration

Python Kerberos Vault Integrator is a package that provides seamless integration between Python applications and the Kerberos Vault. It simplifies the process of receiving messages or videos from the Kerberos Vault. It abstracts the way to communicate with Kerberos Vault.

## Installation
To get started with Python Kerberos Vault Integrator, simply install the package using pip and follow the provided documentation for configuration and usage instructions: `pip install python_kerberos_vault_integrator`

To import the `KerberosVaultIntegrator` class into your Python file, use the following import statement:
`from python_kerberos_vault_integrator import KerberosVaultIntegrator`

## Example usage
The code snippet provided demonstrates the usage of the KerberosVaultQueueReader library in Python. It showcases how to initialize a connection to the Kerberos Vault. The library abstracts away the complexities of interacting with the Kerberos Vault.

```Python
from python_kerberos_vault_integrator.KerberosVaultIntegrator import KerberosVaultIntegrator

# Initialize Kerberos Vault Integrator
kerberos_vault_integrator = KerberosVaultIntegrator('storage_uri_example', 'storage_access_key_example', 'storage_secret_example')

# Process messages until successful response is received or all messages are processed
for body in messages:

    # Update storage-related information if available in message payload
    if "data" in body:
        kerberos_vault_integrator.update_storage_info(body['data'])

    # Create headers for accessing storage service
    headers = kerberos_vault_integrator.create_headers(body['payload']['key'], body['source'])

    try:
        # Fetch data associated with the message from storage service
        resp = requests.get(kerberos_vault_integrator.storage_uri + "/storage/blob", headers=headers, timeout=10)

        if resp is None or resp.status_code != 200:
            print('None response or non-200 status code, skipping...')
            continue

        return resp
        
    except Exception as x:
        print('Error occurred while trying to fetch data from storage:')
        print(x)
        pass
```

## Features
The `KerberosVaultIntegrator` has a couple of useful features such as:

### Initialization
Simply initialize the Kerberos Vault connection using your storage_uri, storage_access_key and storage_secret_key. 
`integrator = KerberosVaultIntegrator(storage_uri, storage_access_key, storage_secret_key)`

### Update storage information

The `update_storage_information` function in the `KerberosVaultIntegrator` class is responsible for updating the storage information used for connecting to the Kerberos Vault. It takes a single dictionary with the key-value pairs of the following parameters.

- `storage_uri` (str): The URI of the storage where the Kerberos Vault is located.
- `storage_access_key` (str): The access key for the storage.
- `storage_secret_key` (str): The secret key for the storage.

### CreateHeaders Function

The `CreateHeaders` function in the `KerberosVaultIntegrator` class is responsible for creating the headers required for authentication with the Kerberos Vault API. It takes the following parameters:

- `file_name` (str): The name of the file to be stored.
- `storage_provider` (str): The name of the storage provider.

The function returns a dictionary containing the headers to be used in the API request.
