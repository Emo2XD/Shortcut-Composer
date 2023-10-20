# SPDX-FileCopyrightText: © 2022-2023 Wojciech Trybus <wojtryb@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

from api_krita import Krita
from api_krita.pyqt import Text
from ..controller_base import Controller


class CanvasBasedController:
    """Family of controllers which operate on values from active document."""

    def refresh(self):
        """Refresh currently stored canvas."""
        self.canvas = Krita.get_active_canvas()


class CanvasZoomController(CanvasBasedController, Controller[int]):
    """
    Gives access to `zoom` in %.

    - Operates on `int`
    - Defaults to `100`
    """

    TYPE = int
    DEFAULT_VALUE: float = 100

    def get_value(self) -> int:
        """Get current zoom level in %"""
        return round(self.canvas.zoom)

    def set_value(self, value: int) -> None:
        """Set current zoom level in %"""
        self.canvas.zoom = value

    def get_label(self, value: int) -> Text:
        """Return Text with formatted canvas zoom."""
        return Text(self.get_pretty_name(value))

    def get_pretty_name(self, value: int) -> str:
        """Format the canvas zoom like: `100%`."""
        return f"{round(value)}%"


class CanvasRotationController(CanvasBasedController, Controller[int]):
    """
    Gives access to `canvas rotation` in degrees.

    - Operates on `int` in range `0 to 360`
    - Other values are expressed in that range
    - Defaults to `0`
    """

    TYPE = int
    DEFAULT_VALUE: float = 0

    def get_value(self) -> int:
        """Get canvas rotation in degrees."""
        return round(self.canvas.rotation)

    def set_value(self, value: int) -> None:
        """Set rotation in degrees."""
        self.canvas.rotation = value

    def get_label(self, value: int) -> Text:
        """Return Text with formatted canvas rotation."""
        return Text(self.get_pretty_name(value))

    def get_pretty_name(self, value: int) -> str:
        """Format the canvas rotation like: `30°`."""
        return f"{round(value)}°"
