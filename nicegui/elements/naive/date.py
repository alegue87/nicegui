from typing import Any, Callable, Dict, List, Optional, Union

from ..mixins.disableable_element import DisableableElement

class DateNve(DisableableElement, component='daten.js'):

    def __init__(self,
                 value: Optional[
                     Union[str, Dict[str, str], List[str], List[Union[str, Dict[str, str]]]]
                 ] = None,
                 *,
                 mask: str = 'MM-dd-yyyy',
                 on_change: Optional[Callable[..., Any]] = None) -> None:
        """Date Input

        ui.dateNve('04-30-2020  01:02:03', mask='MM-dd-yyyy HH:mm:ss', on_change=lambda e: ui.notify(e.args[1])).props('type="datetime"')
            args[1] = '04-09-2020 01:02:03'
            args[0] = timestamp


        :param value: the initial date
        :param mask: the format of the date string (default: 'YYYY-MM-DD')
        :param on_change: callback to execute when changing the date
        """
        super().__init__()
        self._props['value'] = value
        self._props['value-format'] = mask
        self._props['format'] = mask


        self.on('update:value', lambda e : on_change(e))
