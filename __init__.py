"""Init Renpho sensor."""
from .const import DOMAIN, CONF_SWITCH1, CONF_SWITCH2, CONF_INTERFACE
from switchbot import Switchbot

def setup(hass, config):

  conf = config[DOMAIN]
  switch1_mac = conf[CONF_SWITCH1]
  switch2_mac = conf[CONF_SWITCH2]
  interface = conf[CONF_INTERFACE]

  switch1 = Switchbot(switch1_mac, None, interface)
  switch2 = Switchbot(switch2_mac, None, interface)

  hass.data[DOMAIN] = {
    "switch1": switch1,
    "switch2": switch2
  }

  return True