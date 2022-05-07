"""Support for Switchbot bot."""
from switchbot import Switchbot  # pylint: disable=import-error

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import DOMAIN


from homeassistant.components.switch import (
    SwitchEntity,
)


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: None

) -> None:
    """Set up the sensor platform."""

    switches = hass.data[DOMAIN]

    add_entities([DoubleSwitch(switches)])


class DoubleSwitch(SwitchEntity):
    def __init__(self, switches):
        self._switch1 = switches["switch1"]
        self._switch2 = switches["switch2"] 
        """Better to assume on than off at startup"""
        self._is_on = True

    @property   
    def name(self):
        """Name of the entity."""
        return "DoubleSwitch"

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._switch2.hand_down()
        self._switch1.hand_up()
        self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        """We try three times, as 2 normally does it but 1 will not"""
        self._switch2.hand_up()
        self._switch1.hand_down()

        self._switch2.hand_up()
        self._switch1.hand_down()

        self._switch2.hand_up()
        self._switch1.hand_down()

        self._is_on = False