"""Main py loading the integration."""
# __init__.py

import logging

from homeassistant.helpers import config_entry_oauth2_flow
#from .config_flow import ConfigFlow


DOMAIN = "fortmes_energy"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the fortmes-energy integration."""
    logging.info("Empty setup started")
    return True

async def async_setup_entry(hass, config_entry):
    """Set up the fortmes-energy integration."""
    logging.info("Started setup_entry")
    # auth_instance = hass.data[DOMAIN]['auth']
    # device_code, user_code, authorization_uri = await auth_instance.device_authorization()

    if config_entry.data.get("flow_id"):
        logging.info("Setup finished")
        ## At this point the configuration is on the next step
        ### Needs to validate token and fail if something goes wrong.
        #auth_instance = hass.data[DOMAIN]['auth']
        #device_code, user_code, authorization_uri = await auth_instance.device_authorization()
        #logging.info(user_code)


    return True
