"""Life360 Sensor."""

from __future__ import annotations

from typing import override

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .coordinator import L360ConfigEntry
from .entity import Life360MemberEntity, async_setup_member_entities


async def async_setup_entry(
    hass: HomeAssistant,
    entry: L360ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    await async_setup_member_entities(
        hass, entry, async_add_entities, Life360BatterySensor
    )


class Life360BatterySensor(Life360MemberEntity, SensorEntity):
    """Life360 Member battery level."""

    _attr_device_class = SensorDeviceClass.BATTERY
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class = SensorStateClass.MEASUREMENT
    _name_suffix = "Battery"

    @override
    @property
    def native_value(self) -> int | None:
        """Return battery level, if location data is available."""
        if not (loc := self.coordinator.data.loc):
            return None
        return loc.battery_level
