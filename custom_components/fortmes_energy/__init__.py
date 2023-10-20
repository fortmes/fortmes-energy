"""Main py loading the integration."""
# __init__.py

import logging

from homeassistant.helpers import config_entry_oauth2_flow
from fortmes_pypi import Auth0DeviceAuth  # Import your package

DOMAIN = "fortmes_energy"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the fortmes-energy integration."""
    logging.info("Empty setup started")
    # Your integration setup code here
    return True

async def async_setup_entry(hass, config_entry):
    """Set up the fortmes-energy integration."""
    logging.info("Started setup with init")

    if config_entry.data.get("flow_id"):
        implementation = await config_entry_oauth2_flow.async_get_config_entry_implementation(
            hass, config_entry
        )
        auth = Auth0DeviceAuth(
            implementation.client_id,
            implementation.auth0_domain
        )

        # Your code to interact with your Python package goes here
        tokens = await auth.authenticate()
        logging.info(tokens)
        # Use the tokens or do other integration-specific tasks

    return True
