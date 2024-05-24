# Python Kerberos Vault

Python Kerberos Vault is a package that provides seamless integration between Python applications and the Kerberos Vault. It simplifies the process of receiving messages or videos from the Kerberos Vault.

## Installation
To get started with Python Kerberos Vault, simply install the package using pip and follow the provided documentation for configuration and usage instructions: `pip install uugai_python_kerberos_vault`

To import the `KerberosVault` class into your Python file, use the following import statement:
`from uugai_python_kerberos_vault import KerberosVault`

## Message object architecture
The message architecture should match this architecture:

```
{'source': 'your_storage_provider', 
 'payload': {'key': 'file_name', 'additional_info: '...'},
 'data': {storage_uri: 'kerberos_vault_uri' , storage_access_key: 'access_key' , storage_secret: 'secret_key'}
 }
```

## Features
`KerberosVault` has a couple of useful features such as:

### Initialization
Simply initialize the Kerberos Vault connection using your storage_uri, storage_access_key and storage_secret_key. 
`integrator = KerberosVault(storage_uri, storage_access_key, storage_secret_key)`

### Retrieve media
The retrieve_media function is a method of the `KerberosVault` class. It fetches associated data from storage and performs actions based on the provided parameters. It returns the response from the request.get method.

Parameters:

* `message` (str): The message to be processed.
* `media_type` (str): The type of message to be processed (image, video). Default is an empty string.
* `media_savepath` (str): The path where the media file is to be saved. Default is an empty string.

The function first updates the storage-related information if available in the message payload. Then, it creates headers for accessing the storage service using the create_headers method of the class. Make sure the message's architecture matches the above mentioned architecture!

* media_type == 'image': To be implemented

* media_type == 'video': It reconstructs a video file from the received requested data and saves it to the specified media_savepath. `resp = retrieve_media(message, media_type, media_savepath)`

* media_type not provided or supported: No actions are taken on the response object. solely the response is returned.

### Update storage information
The `update_storage_information` function in the `KerberosVault` class is responsible for updating the storage information used for connecting to the Kerberos Vault. It takes a single dictionary with the key-value pairs of the following parameters.

- `storage_uri` (str): The URI of the storage where the Kerberos Vault is located.
- `storage_access_key` (str): The access key for the storage.
- `storage_secret_key` (str): The secret key for the storage.

it could look something like this:
```python
data = {'storage_uri': 'kerberos_vault_uri', 
        'storage_access_key': 'username', 
        'storage_secret_key': 'password'}
update_storage_info(data)
```

### Create headers
The `create_headers()` function in the `KerberosVault` class is responsible for creating the headers required for authentication with the Kerberos Vault API. It takes the following parameters:

- `file_name` (str): The name of the file to request.
- `storage_provider` (str): The name of the storage provider.

The function returns a dictionary containing the headers to be used in the API request.

## Example usage
The code snippet provided demonstrates the usage of the KerberosVault library in Python. It showcases how to initialize a connection and retrieve a media object from the Kerberos Vault. 

```Python
from uugai_python_dynamic_queue.MessageBrokers import RabbitMQ
from uugai_python_kerberos_vault.KerberosVault import KerberosVault

# Initialize a message broker using the python_queue_reader package
rabbitmq = RabbitMQ(queue_name='queue_name_example', 
                    target_queue_name = '', 
                    exchange='', 
                    host='host_name_example', 
                    username='username',
                    password='password')

# Initialize Kerberos Vault
kerberos_vault = KerberosVault('vault_api', 'access_key', 'secret_key')

# Receive messages from the queue
message = rabbitmq.receive_message()

media_type = 'video'
media_savepath = 'data/video.mp4'

# Retrieve media from the Kerberos Vault
resp = kerberos_vault.retrieve_media(message, media_type, media_savepath)
print("media of type", media_type, "saved to location: ", media_savepath)
```
