import logging

DOMAIN = "ezplug"

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    hass.states.set("ezplug.integration", "Ready")

    _LOGGER.info("EZPLUG Ready!")
    _LOGGER.info("Made by delfigamer11")

    # Return boolean to indicate that initialization was successful.
    return True
