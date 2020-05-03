# Globo ACL API Integration Pack

The StackStorm Globo ACL API integration package allows you to create and change ACLs in the Globo ACL API

## Prerequisites

Globo ACL API and Stackstorm, up and running.

## Setup

### Install Globo ACL API pack on StackStorm

Install the [Globo ACL API pack](https://github.com/ribeiro-rodrigo/stackstorm-acl-api.git):

    ```
    # Install AWS
    st2 pack install https://github.com/ribeiro-rodrigo/stackstorm-acl-api.git

    # Check it
    st2 pack get globo_acl_api
    ```
## Actions

Once you have installed the Globo ACL API pack, you can get a list of actions in the ACL API pack using:

```
st2 action list -p globo_acl_api
```

To get information on a specific action, please run:

```
root@3bd64cb6976c:/# st2 action get globo_acl_api.access_create
+---------------+--------------------------------------------------------------+
| Property      | Value                                                        |
+---------------+--------------------------------------------------------------+
| id            | 5e8b444fa41de8012568f662                                     |
| uid           | action:globo_acl_api:access_create                           |
| ref           | globo_acl_api.access_create                                  |
| pack          | globo_acl_api                                                |
| name          | access_create                                                |
| description   | Create Access                                                |
| enabled       | True                                                         |
| entry_point   | access_create.py                                             |
| runner_type   | python-script                                                |
| parameters    | {                                                            |
|               |     "dest_port_start": {                                     |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Destination home port that will      |
|               | receive the defined rule"                                    |
|               |     },                                                       |
|               |     "src_port_op": {                                         |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Accepts the operation values eq,     |
|               | range, lt and gt"                                            |
|               |     },                                                       |
|               |     "protocol": {                                            |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "Access protocol. Valid values are:   |
|               | ip, tcp, udp, icmp. If defined"                              |
|               |     },                                                       |
|               |     "dest_port_end": {                                       |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Final destination port that will     |
|               | receive the rule"                                            |
|               |     },                                                       |
|               |     "url": {                                                 |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "URL ACL API"                         |
|               |     },                                                       |
|               |     "destination": {                                         |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "Access destination address. Only     |
|               | IPv4 and IPV6 addresses are accepted and they must be        |
|               | registered within NetworkAPI"                                |
|               |     },                                                       |
|               |     "source": {                                              |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "Access source address. Only IPv4 and |
|               | IPV6 addresses are accepted and they must be registered      |
|               | within the network informed in the URI"                      |
|               |     },                                                       |
|               |     "dest_port_op": {                                        |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Accepts the operation values eq,     |
|               | range, lt and gt"                                            |
|               |     },                                                       |
|               |     "action": {                                              |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "Access action. Valid values are:     |
|               | permit or deny"                                              |
|               |     },                                                       |
|               |     "basickey": {                                            |
|               |         "required": true,                                    |
|               |         "type": "string",                                    |
|               |         "description": "Authorization Basic base64"          |
|               |     },                                                       |
|               |     "src_port_end": {                                        |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Final source port that will receive  |
|               | the rule"                                                    |
|               |     },                                                       |
|               |     "src_port_start": {                                      |
|               |         "required": false,                                   |
|               |         "type": "string",                                    |
|               |         "description": "Initial port of the source that will |
|               | receive the defined rule"                                    |
|               |     }                                                        |
|               | }                                                            |
| metadata_file | actions/access_create.yaml                                   |
| notify        |                                                              |
| output_schema |                                                              |
| tags          |                                                              |
+---------------+--------------------------------------------------------------+


```
