"""conflig flow handing the install."""

import logging
#import asyncio
import voluptuous as vol
#import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
#from homeassistant.helpers import config_entry_oauth2_flow
from fortmes_pypi import Auth0Client  # Import your package
from requests.exceptions import HTTPError

DOMAIN = "fortmes_energy"

_LOGGER = logging.getLogger(__name__)

# async def async_setup(hass, config):
#     """Set up the fortmes-energy integration."""
#     _LOGGER.info("Empty setup started2")
#     # Your integration setup code here

#     return True

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for fortmes-energy."""
    data = {}


    def __init__(self) -> None:
        self.auth = Auth0Client()



    async def async_step_user(self, user_input=None):
        """Config flow for fortmes-energy."""
        flow_id = self.flow_id
        errors = {}
        user_code = ''
        _LOGGER.info("User flow started with id %s", flow_id)
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        #Abort if Device is already configured
        # await self.async_set_unique_id(device_unique_id)
        # self._abort_if_unique_id_configured()
        if user_input is not None:
            _LOGGER.info("Ready for next step")

            self.data.update({
                    "flow_id": flow_id
                })
            return await self.async_step_validate()

        # Display the user input form
        device_code, user_code, authorization_uri = await self.auth.device_authorization()
        _LOGGER.info("The device code is: '%s' and the user-code is '%s' and the auth uri is '%s'",device_code, user_code, authorization_uri)

        # ?user_code=QTZL-MCBW
        return self.async_show_form(step_id="user", data_schema=None, description_placeholders={ 'next_button': 'Next',"user_code": user_code, "authorization_uri": authorization_uri}, errors=errors)

    async def async_step_validate(self, access_token=None):
        ## Wait until the config is done
        errors = {}
        access_token = ""

        try:
            access_token = await self.auth.token_validation()
            #access_token.raise_for_status()
            _LOGGER.info(access_token)
            self.data.update({
                "access_token": access_token
            })

        except Exception as e:
            # Handle any other exceptions

            _LOGGER.error("Exception general error: %s", e)
            return self.async_abort(reason="authentication_notfinished")



        if access_token is not None:
            # Validate user input and create/update config entry here
            # Return the config entry data
            _LOGGER.info("User_input is the following %s!", self.data)
            self.hass.data.setdefault(DOMAIN, {})
            self.hass.data[DOMAIN]['auth'] = self.auth
            return self.async_create_entry(title="Fortmes Energy", data=self.data)
        # if done print status
        return self.async_show_form(step_id="validate", data_schema=None,  errors=errors)
