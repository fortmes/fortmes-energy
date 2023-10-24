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

async def async_setup(hass, config):
    """Set up the fortmes-energy integration."""
    _LOGGER.info("Empty setup started2")
    # Your integration setup code here

    return True

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for fortmes-energy."""
    #VERSION = 1

    def __init__(self) -> None:
        self.auth = self._start_auth0_device_auth()
        #self.auth = Auth0Client()
        self.user_code = ''

    async def async_step_user(self, user_input=None):
        """Config flow for fortmes-energy."""
        flow_id = self.flow_id
        _LOGGER.info("User flow started with id %s", flow_id)

        #Abort if Device is already configured
        # await self.async_set_unique_id(device_unique_id)
        # self._abort_if_unique_id_configured()
        if user_input is not None:
            _LOGGER.info("Ready for next step")
            user_input["flow_id"] = flow_id
            return await self.async_step_validate()

        # Display the user input form
        device_code, self.user_code, authorization_uri = await self.auth.device_authorization()
        _LOGGER.info("The device code is: '%s' and the user-code is '%s' and the auth uri is '%s'",device_code, self.user_code, authorization_uri)

        # ?user_code=QTZL-MCBW
        return self.async_show_form(step_id="user", data_schema=None, description_placeholders={ 'next_button': 'Next',"user_code": self.user_code, "authorization_uri": authorization_uri})

    async def async_step_validate(self, user_input=None):
        ## Wait until the config is done
        errors=[]
        access_token = ""

        try:
            user_input = {}
            access_token = await self.auth.token_validation()
            #access_token.raise_for_status()
            user_input["access_token"] = access_token
            _LOGGER.info(access_token)

        except Exception as e:
            # Handle any other exceptions
            #errors[0] = "authentication_notfinished"
            _LOGGER.error("Exception general error: %s", e)



        if user_input is not None:
            # Validate user input and create/update config entry here
            # Return the config entry data
            _LOGGER.info(self)
            final_data = {**self.context["user_input"], **user_input}
            _LOGGER.info("User_input is the following %s!", final_data)
            self.hass.data.setdefault(DOMAIN, {})
            #self.hass.data[DOMAIN]['auth'] = self.auth
            return self.async_create_entry(title="Fortmes Energy", data=final_data)
        # if done print status
        return self.async_show_form(step_id="validate", data_schema=None,  errors=errors)

### not needed anymore
    def _start_auth0_device_auth(self):
            """This function initializes the class for authentication."""
            # Make an HTTP request to Auth0 to start the Device Authorization Flow
            # Obtain the device code and verification URI
            client_id = "WxzBvwjGrWyjhcNs9vSH9dPqhE5mFplS" # This is DEV app
            auth0_domain = "dev-fortmes.eu.auth0.com" ### This is DEV tenant
            return Auth0Client(
            auth0_domain, client_id
        )
