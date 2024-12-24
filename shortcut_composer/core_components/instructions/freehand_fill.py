from api_krita import Krita
from api_krita.enums.action import Action
from ..instruction_base import Instruction

class FillOnRelease(Instruction):
    """
    Fill on release key
    """

    def on_every_key_release(self) -> None:
        # TODO you have to ensure there is a selection. Avoid filling whole image
        # currently assign this function in ctrl+F
        Krita.trigger_action(Action.FILL_WITH_FOREGROUND_COLOUR.value)