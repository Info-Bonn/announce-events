import os
import logging

### @package environment
#
# Interacitons with the environment variables.
#

def load_env(key: str, default: str) -> str:
    """!
    os.getenv() wrapper that handles the case of None-types for not-set env-variables\n

    @param key: name of env variable to load
    @param default: default value if variable couldn't be loaded
    @return value of env variable or default value
    """
    value = os.getenv(key)
    if value:
        return value
    print(f"Can't load env-variable for: '{key}' - falling back to DEFAULT {key}='{default}'")
    logger.warning(f"Can't load env-variable for: '{key}' - falling back to DEFAULT {key}='{default}'")
    return default


logger = logging.getLogger('my-bot')

TOKEN = os.getenv("TOKEN")  # reading in the token from config.py file

# loading optional env variables
PREFIX = load_env("PREFIX", "a!")
VERSION = load_env("VERSION", "unknown")  # version of the bot
OWNER_NAME = load_env("OWNER_NAME", "unknown")   # owner name with tag e.g. pi#3141
OWNER_ID = int(load_env("OWNER_ID", "100000000000000000"))  # discord id of the owner

# defaults are set for Info Bonn Server
EVENT_ROLE = int(load_env("EVENT_ROLE", "855395051046436885"))  # id of the role to be pinged in event announcement
EVENT_CHANNEL = int(load_env("EVENT_CHANNEL", "760490896298082314"))  # id of channel to send announcement into
ROLE_EVENT_HOST = int(load_env("ROLE_EVENT_HOST", "855397441784250368"))  # role of event hosts for permission check
