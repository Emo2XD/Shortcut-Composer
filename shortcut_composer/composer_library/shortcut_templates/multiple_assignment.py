from typing import Any, Iterable, List, Optional
from dataclasses import field, dataclass
from itertools import cycle

from ..krita_api.controllers import Controller
from ..shortcut_connection_utils import PluginAction


@dataclass
class MultipleAssignment(PluginAction):
    """
    Abstract class with custom key event interface for cyclic actions

    Action cycles around passed 'values_to_cycle':

    - before the cycle starts, long press works as 'temporary key'
    - then, short key press moves to next value.
    - end of long press moves to passed 'default value'

    Child class has to define how to set and determine value:
    - set_value
    - get_current_value
    """

    controller: Controller
    values_to_cycle: List[Any]
    default_value: Any = None
    time_interval: float = 0.3

    _last_value: Any = field(init=False, default=None)
    _iterator: Optional[Iterable] = field(init=False, default=None)

    def __post_init__(self):
        """
        Create flag determining that cycling just started.

        If default_value should be taken into consideration, it's simply
        added to the end of cycle list.
        """
        if self.default_value is None:
            self.default_value = self.controller.default_value

    def on_key_press(self):
        """Use key press event only for switching to first value."""
        current_value = self.controller.get_value()
        if current_value != self._last_value:
            self._reset_iterator()
        self._set_value(next(self._iterator))

    def on_long_key_release(self):
        """All long releases set default value."""
        self._set_value(self.default_value)
        self._reset_iterator()

    def _set_value(self, value: Any):
        self._last_value = value
        self.controller.set_value(value)

    def _reset_iterator(self):
        self._iterator = cycle(self.values_to_cycle)
