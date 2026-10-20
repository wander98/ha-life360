"""Life360 per-Member entities (battery and charging)."""

from __future__ import annotations

import asyncio
from collections.abc import Callable
import logging
from typing import override

from homeassistant.core import HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import ATTRIBUTION, SIGNAL_MEMBERS_CHANGED
from .coordinator import L360ConfigEntry, MemberDataUpdateCoordinator
from .helpers import MemberID

_LOGGER = logging.getLogger(__name__)


class Life360MemberEntity(CoordinatorEntity[MemberDataUpdateCoordinator]):
    """Base for entities that report one Member's data."""

    _attr_attribution = ATTRIBUTION
    _name_suffix: str

    def __init__(self, coordinator: MemberDataUpdateCoordinator, mid: MemberID) -> None:
        """Initialize entity."""
        super().__init__(coordinator)
        self._attr_unique_id = f"{mid}_{self._name_suffix.lower()}"
        self._update_name()

    @override
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._update_name()
        super()._handle_coordinator_update()

    def _update_name(self) -> None:
        """Update name from Member's name, like the device tracker does."""
        name = self.coordinator.data.details.name
        self._attr_name = f"Life360 {name} {self._name_suffix}"


async def async_setup_member_entities(
    hass: HomeAssistant,
    entry: L360ConfigEntry,
    async_add_entities: AddEntitiesCallback,
    factory: Callable[[MemberDataUpdateCoordinator, MemberID], Entity],
) -> None:
    """Add and remove per-Member entities as Members come and go."""
    coordinator = entry.runtime_data.coordinator
    mem_coordinator = entry.runtime_data.mem_coordinator
    entities: dict[MemberID, Entity] = {}

    async def async_process_data() -> None:
        """Process Members."""
        mids = set(coordinator.data.mem_details)
        if del_mids := set(entities) - mids:
            old_entities = [entities.pop(mid) for mid in del_mids]
            await asyncio.gather(
                *(entity.async_remove() for entity in old_entities if entity.enabled)
            )
        if add_mids := mids - set(entities):
            new_entities = {mid: factory(mem_coordinator[mid], mid) for mid in add_mids}
            entities.update(new_entities)
            async_add_entities(new_entities.values())

    entry.async_on_unload(
        async_dispatcher_connect(hass, SIGNAL_MEMBERS_CHANGED, async_process_data)
    )
