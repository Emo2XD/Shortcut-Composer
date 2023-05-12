# SPDX-FileCopyrightText: © 2022-2023 Wojciech Trybus <wojtryb@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

from typing import Optional

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import (
    QWidget,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy)

from api_krita import Krita
from api_krita.pyqt import AnimatedWidget, BaseWidget, SafeConfirmButton
from config_system.ui import ConfigFormWidget, ConfigSpinBox
from composer_utils import Config
from ..pie_style import PieStyle
from ..pie_config import PieConfig


class PieSettings(AnimatedWidget, BaseWidget):
    """
    Abstract widget that allows to change values in passed config.

    Meant to be displayed next to the pie menu.

    Consists of two tabs:
    - form with field values to set
    - tab for picking save location

    Subclasses can add additional tabs.
    """

    def __init__(
        self,
        config: PieConfig,
        style: PieStyle,
        parent: Optional[QWidget] = None,
    ) -> None:
        AnimatedWidget.__init__(self, parent, Config.PIE_ANIMATION_TIME.read())
        self.setMinimumHeight(round(style.widget_radius*2))
        self.setAcceptDrops(True)
        self.setWindowFlags((
            self.windowFlags() |  # type: ignore
            Qt.Tool |
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint))
        self.setCursor(Qt.ArrowCursor)

        self._style = style
        self._config = config
        self._config.register_callback(self._reset)

        self._tab_holder = QTabWidget()
        self._local_settings = ConfigFormWidget([
            ConfigSpinBox(config.PIE_RADIUS_SCALE, self, "Pie scale", 0.05, 4),
            ConfigSpinBox(config.ICON_RADIUS_SCALE, self, "Icon max scale",
                          0.05, 4),
        ])
        self._tab_holder.addTab(self._local_settings, "Local settings")
        self._tab_holder.addTab(LocationTab(self._config), "Location")

        layout = QVBoxLayout(self)
        layout.addWidget(self._tab_holder)
        self.setLayout(layout)

    def show(self):
        """Show the window after its settings are refreshed."""
        self._local_settings.refresh()
        super().show()

    def hide(self) -> None:
        """Hide the window after its settings are saved to kritarc."""
        self._local_settings.apply()
        super().hide()

    def move_to_pie_side(self):
        """Move the widget on the right side of the pie."""
        offset = self.width()//2 + self._style.widget_radius * 1.05
        point = QPoint(round(offset), 0)
        # HACK Assume the pie center should be at the cursor
        self.move_center(QCursor().pos() + point)  # type: ignore

    def _reset(self):
        """React to change in pie size."""
        self.setMinimumHeight(self._style.widget_radius*2)


class LocationTab(QWidget):
    """PieSettings tab for changing location in which values are saved."""

    def __init__(
        self,
        config: PieConfig,
        parent: Optional[QWidget] = None
    ) -> None:
        """Tab that allows to switch location in which icon order is saved."""
        super().__init__(parent)
        self._config = config

        self._location_button = self._init_location_button()
        self._mode_title = self._init_mode_title()
        self._mode_description = self._init_mode_description()
        self._reset_default_button = self._init_set_default_button()

        self._init_layout()
        self.is_local_mode = self._config.SAVE_LOCAL.read()

    def _init_layout(self):
        """
        Create and set a layout of the tab.

        - Header holds a button for switching save locations.
        - Main area consists of labels describing active location.
        - Footer consists of buttons with additional value management
          actions.
        """
        header = QHBoxLayout()
        header.addWidget(QLabel(text="Save location:"), 2, Qt.AlignCenter)
        header.addWidget(self._location_button, 1)

        layout = QVBoxLayout()
        layout.addLayout(header)
        layout.addWidget(self._mode_title)
        layout.addWidget(self._mode_description)
        layout.addStretch()
        layout.addWidget(self._reset_default_button)
        self.setLayout(layout)

    def _init_location_button(self) -> SafeConfirmButton:
        """Return button that switches between save locations."""
        def switch_mode():
            values = self._config.ORDER.read()

            self.is_local_mode = not self.is_local_mode
            if self.is_local_mode:
                self._config.reset_the_default()

            # make sure the icons stay the same
            self._config.ORDER.write(values)

        location_button = SafeConfirmButton(text="Change mode")
        location_button.clicked.connect(switch_mode)
        location_button.setFixedHeight(location_button.sizeHint().height()*2)
        return location_button

    def _init_mode_title(self) -> QLabel:
        """Return QLabel with one-line description of the active mode."""
        mode_title = QLabel()
        mode_title.setStyleSheet("font-weight: bold")
        mode_title.setAlignment(Qt.AlignHCenter)
        mode_title.setWordWrap(True)
        mode_title.setSizePolicy(
            QSizePolicy.Ignored,
            QSizePolicy.Ignored)
        return mode_title

    def _init_mode_description(self) -> QLabel:
        """Return QLabel with onedetailed description of the active mode."""
        mode_description = QLabel()
        mode_description.setSizePolicy(
            QSizePolicy.Ignored,
            QSizePolicy.Ignored)
        mode_description.setWordWrap(True)
        return mode_description

    def _init_set_default_button(self) -> SafeConfirmButton:
        """Return button saving currently active values as the default ones."""
        default_button = SafeConfirmButton(text="Set current as default")
        default_button.clicked.connect(self._config.set_current_as_default)
        default_button.setFixedHeight(default_button.sizeHint().height()*2)
        return default_button

    @property
    def is_local_mode(self) -> bool:
        """Return whether pie saves the values locally."""
        return self._config.SAVE_LOCAL.read()

    @is_local_mode.setter
    def is_local_mode(self, value: bool) -> None:
        """Return whether pie should save the values locally."""
        if value:
            self._location_button.main_text = "Local"
            self._location_button.icon = Krita.get_icon("folder-documents")
            self._mode_title.setText(
                "Pie values are saved in the .kra document\n")
            self._mode_description.setText(
                "Each new document starts with the default set of "
                "values which are can to be modified to those used "
                "in given file the most.\n\n"

                "Saved values are not lost between sessions.\n\n"

                "Switching between documents, results in pie switching "
                "the values to those saved in the active document.\n\n"

                "For resources, only resource names are stored. "
                "Saved value will be lost, when the resource is missing.")
            self._reset_default_button.setEnabled(True)
        else:
            self._location_button.main_text = "Global"
            self._location_button.icon = Krita.get_icon("properties")
            self._mode_title.setText(
                "Pie values are saved in krita settings.\n")
            self._mode_description.setText(
                "Values remain the same until modified by the user.\t\t"

                "Selected values and their order is saved between "
                "sessions. This mode is meant to be used for values that"
                "remain useful regardless of which document is edited.")
            self._reset_default_button.setDisabled(True)
        self._config.SAVE_LOCAL.write(value)
