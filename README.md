Cloudhealth REST Client
=======================

This is a Python REST Client for the Cloudhealth service.

## Installation

```shell
pip install cloudhealth-client

# Clone repo
git clone https://github.com/albertonarro/cloudhealth-client.git
```


## Python Usage

```python
from cloudhealth-client import client

ch = client.CloudHealth(api_key='Ali23melAS$E#@$Im3lsim1!')

# Get AWS instance usage for yesterday (currently only AWS is supported)
ch.usage.get(resource_type='instance')
...

79.79166666666666

# Get current cost of all service in all AWS-Accounts
ch.cost.get_current(account_type='AWS-Account')
...

9676.619999999908

```


## Testing

[!WIP]

## Contributions..

[!WIP]
