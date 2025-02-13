# -*- coding: utf-8 -*-
# -*- Python Version: 3.7 -*-

"""Model class for the Ventilation worksheet various input items."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

from PHX.xl import xl_data
from PHX.xl.xl_data import xl_writable
from PHX.PHPP.phpp_localization import shape_model


@dataclass
class VentilationInputItem:
    """Ventilation Worksheet input item."""

    shape: shape_model.Ventilation
    input_data: xl_writable
    input_type: str = field(init=False)
    input_unit: Optional[str] = None
    target_unit: Optional[str] = None

    def create_xl_item(self, _sheet_name: str, _row_num: int) -> xl_data.XlItem:
        """Returns a list of the XL Items to write for this Surface Entry

        Arguments:
        ----------
            * _sheet_name: (str) The name of the worksheet to write to.
            * _row_num: (int) The row number to build the XlItems for

        Returns:
        --------
            * (XlItem): The XlItem to write to the sheet.
        """
        return xl_data.XlItem(
            sheet_name=_sheet_name,
            xl_range=f"{getattr(self.shape, self.input_type).input_column}{_row_num}",
            write_value=self.input_data,
            input_unit=self.input_unit,
            target_unit=self.target_unit,
        )

    @classmethod
    def vent_type(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "vent_type"
        return obj

    @classmethod
    def multi_unit_on(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "multi_unit_on"
        return obj

    @classmethod
    def wind_coeff_e(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "wind_coeff_e"
        return obj

    @classmethod
    def wind_coeff_f(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "wind_coeff_f"
        return obj

    @classmethod
    def airtightness_n50(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "airtightness_n50"
        return obj

    @classmethod
    def airtightness_Vn50(
        cls, shape: shape_model.Ventilation, input_data: xl_writable
    ) -> VentilationInputItem:
        obj = cls(shape, input_data)
        obj.input_type = "airtightness_Vn50"
        obj.input_unit = "M3"
        obj.target_unit = shape.airtightness_Vn50.unit
        return obj
