"""conflig flow handing the install"""

import logging
import asyncio
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
from homeassistant.helpers import config_entry_oauth2_flow
from fortmes.pypi import Auth0DeviceAuth

DOMAIN = "fortmes_energy"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the fortmes-energy integration."""
    # Your integration setup code here
    return True

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for fortmes-energy."""

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Validate user input and create/update config entry here
            # Return the config entry data

        # Display the user input form
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({
                    vol.Required("client_id"): str,
                    vol.Required("auth0_domain"): str,
                }),
            )
