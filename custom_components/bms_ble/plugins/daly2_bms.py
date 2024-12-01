"""Module to support Daly Smart BMS 2."""

from typing import Any

from bleak.backends.device import BLEDevice

from custom_components.bms_ble.const import (
    ATTR_BATTERY_CHARGING,
    ATTR_CYCLE_CAP,
    ATTR_POWER,
    ATTR_RUNTIME,
    ATTR_TEMPERATURE,
)

from .daly_bms import BMS as DalyBMS


class BMS(DalyBMS):
    """Daly OEM BMS class implementation."""

    def __init__(self, ble_device: BLEDevice, reconnect: bool = False) -> None:
        """Intialize private BMS members."""
        super().__init__(ble_device, reconnect, __name__)

    @staticmethod
    def matcher_dict_list() -> list[dict[str, Any]]:
        """Provide BluetoothMatcher definition."""
        return [
            {
                "manufacturer_id": 770,
                "service_uuid": BMS.uuid_services()[0],
                "connectable": True,
            }
        ]

    @staticmethod
    def device_info() -> dict[str, str]:
        """Return device information for the battery management system."""
        return {"manufacturer": "Daly", "model": "Smart BMS 2"}

    @staticmethod
    def uuid_services() -> list[str]:
        """Return list of 128-bit UUIDs of services required by BMS."""
        return ["02f00000-0000-0000-0000-00000000fe00"]

    @staticmethod
    def uuid_rx() -> str:
        """Return 16-bit UUID of characteristic that provides notification/read property."""
        return DalyBMS.uuid_rx()

    @staticmethod
    def uuid_tx() -> str:
        """Return 16-bit UUID of characteristic that provides write property."""
        return DalyBMS.uuid_tx()

    @staticmethod
    def _calc_values() -> set[str]:
        return {
            ATTR_CYCLE_CAP,
            ATTR_POWER,
            ATTR_BATTERY_CHARGING,
            ATTR_RUNTIME,
            ATTR_TEMPERATURE,
        }
