"""File that acts as config - define all action objects here."""

from .shortcut_library import plugin_actions as templates
from .shortcut_library.plugin_actions import HideStrategy, PickStrategy
from .shortcut_library.api_adapter import controller, Tool, Tag, BlendingMode
from .shortcut_library.api_adapter.controller import SetBrushStrategy
from .shortcut_library.plugin_actions.slider_utils import Slider, Range

actions = [
    templates.TemporaryAction(
        action_name="Eraser (toggle)",
        controller=controller.EraserController(affect_preserve_alpha=True),
        low_value=False,
        high_value=True,
    ),
    templates.TemporaryAction(
        action_name="Preserve alpha (toggle)",
        controller=controller.PreserveAlphaController(affect_eraser=True),
        low_value=False,
        high_value=True,
    ),
    templates.LayerPicker(
        action_name="Layer picker",
        hide_strategy=HideStrategy.MAKE_INVISIBLE,
        pick_strategy=PickStrategy.VISIBLE
    ),
    templates.VirtualSliderAction(
        action_name="Brush size mouse",
        separate_sliders=True,
        horizontal_slider=Slider(
            controller=controller.BrushSizeController(),
            default_value=100,
            values_to_cycle=Range(1, 1000),
            sensitivity=0.5
        ),
        vertical_slider=Slider(
            controller=controller.BrushSizeController(),
            default_value=100,
            values_to_cycle=[50, 100, 200, 250, 500, 1000]
        ),
    ),
    templates.VirtualSliderAction(
        action_name="Mouse cycle",
        separate_sliders=True,
        horizontal_slider=Slider(
            controller=controller.OpacityController(),
            default_value=50,
            values_to_cycle=Range(10, 90)
        ),
        vertical_slider=Slider(
            controller=controller.OpacityController(),
            default_value=50,
            values_to_cycle=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        ),
        # horizontal_slider=Slider(
        #     controller=controller.ToolController,
        #     default_value=Tool.FREEHAND_SELECTION,
        #     values_to_cycle=[
        #         Tool.FREEHAND_SELECTION,
        #         Tool.RECTANGULAR_SELECTION,
        #         Tool.CONTIGUOUS_SELECTION,
        #         Tool.GRADIENT,
        #         Tool.LINE,
        #         Tool.TRANSFORM,
        #         Tool.REFERENCE,
        #     ],
        # ),
        # vertical_slider=Slider(
        #     controller=controller.BlendingModeController(),
        #     values_to_cycle=[
        #         BlendingMode.OVERLAY,
        #         BlendingMode.NORMAL,
        #         BlendingMode.DARKEN],
        #     default_value=BlendingMode.NORMAL,
        #     sensitivity=50
        # ),
    ),
    templates.VirtualSliderAction(
        action_name="Canvas slider",
        separate_sliders=True,
        horizontal_slider=Slider(
            controller=controller.CanvasRotationController(),
            default_value=0,
            values_to_cycle=Range(1, 90),
            sensitivity=50
        ),
        vertical_slider=Slider(
            controller=controller.CanvasZoomController(),
            default_value=1,
            values_to_cycle=Range(0.25, 4),
            sensitivity=50
        ),
    ),
    templates.TemporaryAction(
        action_name="Freehand selection (toggle)",
        controller=controller.ToolController(),
        high_value=Tool.FREEHAND_SELECTION,
    ),
    templates.TemporaryAction(
        action_name="Gradient (toggle)",
        controller=controller.ToolController(),
        high_value=Tool.GRADIENT,
    ),
    templates.TemporaryAction(
        action_name="Line tool (toggle)",
        controller=controller.ToolController(),
        high_value=Tool.LINE,
    ),
    templates.TemporaryAction(
        action_name="Transform tool (toggle)",
        controller=controller.ToolController(),
        high_value=Tool.TRANSFORM,
        time_interval=1.0
    ),
    templates.TemporaryAction(
        action_name="Move tool (toggle)",
        controller=controller.ToolController(),
        high_value=Tool.MOVE,
    ),
    templates.CyclicAction(
        action_name="Selections tools (cycle)",
        controller=controller.ToolController(),
        values_to_cycle=[
            Tool.FREEHAND_SELECTION,
            Tool.RECTANGULAR_SELECTION,
            Tool.CONTIGUOUS_SELECTION,
        ],
    ),
    templates.CyclicAction(
        action_name="Canvas cycle",
        controller=controller.CanvasRotationController(),
        default_value=0,
        values_to_cycle=[15, 30, 60, 90],
    ),
    templates.CyclicAction(
        action_name="Misc tools (cycle)",
        controller=controller.ToolController(),
        values_to_cycle=[
            Tool.GRADIENT,
            Tool.LINE,
            Tool.TRANSFORM,
            Tool.REFERENCE,
        ],
    ),
    templates.CyclicAction(
        action_name="Preset (cycle)",
        controller=controller.PresetController(
            set_brush_strategy=SetBrushStrategy.ON_NON_PAINTABLE
        ),
        default_value="y) Texture Big",
        values_to_cycle=Tag("Digital")
    ),
    templates.CyclicAction(
        action_name="Opacity (cycle)",
        controller=controller.OpacityController(),
        values_to_cycle=[75, 50, 20.3, 11.1],
        include_default_in_cycle=True,
    ),
    templates.CyclicAction(
        action_name="Blending mode (cycle)",
        controller=controller.BlendingModeController(),
        values_to_cycle=[BlendingMode.OVERLAY],
        include_default_in_cycle=True,
    ),
]
