# event announcement bot 
Allow a role to ping another using the bot while everyone else can't ping that role.

This is useful for event hosts which shall be allowed to ping an 'event attandee' role that shoulnd't be pingable for all users.   

## setup
Use the docker environment provided by [@mayniklas](https://github.com/MayNiklas) or start it from your terminal.

Terminal:  
`python3 -m venv venv`  
`venv/bin/python3 -m pip install -r src/requirements.txt`
`export TOKEN="your-key"`  
`venv/bin/python3 src/main.py`  

### needed env variables
| parameter | default |  description |
| ------ |  ------ | ------ |
| `TOKEN` | `NONE` | Your discord bot token |
| `EVENT_ROLE` | `855395051046436885` | ID of the to be pinged by the bot |
| `EVENT_CHANNEL` | `760490896298082314` | Channel the bot shall send the announcement into |
| `ROLE_EVENT_HOST` | `855397441784250368` | ID of the role that is allowed to use the ping command |

#### optional env variables
| parameter | default |  description |
| ------ |  ------ | ------ |
| `Prefix` | `a!`  | Command prefix |
| `VERSION` | `unknown` | Version the bot is running |
| `OWNER_NAME` | `unknwon` | Name of the bot owner |
| `OWNER_ID` | `100000000000000000` | ID of the bot owner |

The shown values are the default values that will be loaded if nothing else is specified.

## commands
| command | description |
| ------ |  ------ |
| `anc [message]` |  Message will be reposted in defined channel including mention |
| `help` | Display help message |
| `ping` | Show ping |
