# SPDX-FileCopyrightText: © 2022 Wojciech Trybus <wojtryb@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

# from PyQt5.QtWidgets import QWidget

from composer_utils.config import (
    EnumsListField,
    ImmutablesListField,
    ImmutableField,
    FieldBase)
from data_components import Tag


def create_local_config(
    name: str,
    values: list,
    pie_radius_scale: float,
    icon_radius_scale: float,
) -> 'PieConfig':
    args = [name, values, pie_radius_scale, icon_radius_scale]
    if isinstance(values, Tag):
        return PresetPieConfig(*args)
    return EnumPieConfig(*args)


class PieConfig:
    values: list
    order: FieldBase
    # settings_window: QWidget

    def __init__(
        self,
        name: str,
        values: list,
        pie_radius_scale: float,
        icon_radius_scale: float,
    ) -> None:
        self.name = name
        self._default_values = values
        self.pie_radius_scale = ImmutableField(
            f"{self.name} pie scale",
            pie_radius_scale)
        self.icon_radius_scale = ImmutableField(
            f"{self.name} icon scale",
            icon_radius_scale)

    # def create_pie_window(self) -> QWidget: ...

class PresetPieConfig(PieConfig):
    def __init__(self, *args):
        super().__init__(*args)
        self._default_values: Tag
        self.tag_name = ImmutableField(
            self.name, self._default_values.tag_name)
        self.order = ImmutablesListField(f"{self.name} values", [""])

    @property
    def values(self):
        saved_order = self.order.read()
        tag_values = Tag(self.tag_name.read())

        preset_order = [p for p in saved_order if p in tag_values]
        missing = [p for p in tag_values if p not in saved_order]
        return preset_order + missing


class EnumPieConfig(PieConfig):
    def __init__(self, *args):
        super().__init__(*args)
        self.order = EnumsListField(
            f"{self.name} values",
            self._default_values)

    @property
    def values(self):
        return self.order.read()
