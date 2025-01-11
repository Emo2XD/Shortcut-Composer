from api_krita import Krita
from api_krita.enums import Action, BlendingMode
from ..instruction_base import Instruction
from core_components.controllers import BlendingModeStoreGlobalController

class FillOnRelease(Instruction):
    """
    Fill on release key
    """

    def on_every_key_release(self) -> None:
        # TODO you have to ensure there is a selection. Avoid filling whole image
        # currently assign this function in ctrl+F
        Krita.trigger_action(Action.FILL_WITH_FOREGROUND_COLOUR.value)


class ToggleFGBGColor(Instruction):
    """Toggles between foreground color and background color
    """
    is_released = True
    def on_key_press(self) -> None:
        if not ToggleFGBGColor.is_released:
            return
        Krita.trigger_action(Action.SWAP_FOREGROUND_AND_BACKGROUND_COLOURS.value)
        ToggleFGBGColor.is_released = False

    def on_every_key_release(self) -> None:
        Krita.trigger_action(Action.SWAP_FOREGROUND_AND_BACKGROUND_COLOURS.value)
        ToggleFGBGColor.is_released = True


class EnsureEraseBlendingMode(Instruction):
    """Ensure Erase Blending mode
    """
    def on_every_key_release(self) -> None:
        Krita.get_active_view().blending_mode = BlendingMode.ERASE
    # def on_key_press(self) -> None:
    #     Krita.get_active_view().blending_mode = BlendingModeStoreGlobalController.global_blending_mode
        
