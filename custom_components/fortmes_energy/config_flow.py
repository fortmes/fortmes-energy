"""conflig flow handing the install."""

import logging
#import asyncio
import voluptuous as vol
#import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
#from homeassistant.helpers import config_entry_oauth2_flow

DOMAIN = "fortmes_energy"

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the fortmes-energy integration."""
    logging.info("Empty setup started2")
    # Your integration setup code here
    return True

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for fortmes-energy."""

    async def async_step_user(self, user_input=None):
        """Config flow for fortmes-energy."""
        logging.info("User flow started")

        if user_input is not None:
            # Validate user input and create/update config entry here
            # Return the config entry data
             return self.async_create_entry(title="Fortmes Energy", data=user_input)
        # Display the user input form
        device_code, verification_uri = self._start_auth0_device_auth()
        logging.info(device_code)
        return self.async_show_form(step_id="user", data_schema=None, description_placeholders={"device_code": device_code, "verification_uri": verification_uri})

        # return self.async_show_form(
        #     step_id="user",
        #     data_schema=vol.Schema({
        #         vol.Required("client_id"): str,
        #         vol.Required("auth0_domain"): str,
        #     }),
        # )


    def _start_auth0_device_auth(self):
            """This is something nasty"""
            # Make an HTTP request to Auth0 to start the Device Authorization Flow
            # Obtain the device code and verification URI
            device_code = "0 3 4 5 6"
            verification_uri = "https://google.com"
            return device_code, verification_uri
