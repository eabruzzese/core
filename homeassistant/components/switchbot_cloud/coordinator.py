"""Abratractions for using the DataUpdateCoordinator with SwitchBot devices."""

from typing import Any

from switchbot_cloud import SwitchBot

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator


class SwitchBotDataUpdateCoordinator(DataUpdateCoordinator):
    """A thin wrapper around the DataUpdateCoordinator to store an API instance."""

    api: SwitchBot

    def __init__(self, *args: Any, api: SwitchBot, **kwargs: Any) -> None:
        """Store a reference to the SwitchBot API session after configuring the updater."""
        super().__init__(*args, **kwargs)
        self.api = api
