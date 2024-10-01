from typing import Any, Callable, Dict, List, Optional, Union

from ..mixins.disableable_element import DisableableElement

class DateAnt(DisableableElement, component='datea.js'):

    def __init__(self,
                 value: Optional[
                     Union[str, Dict[str, str], List[str], List[Union[str, Dict[str, str]]]]
                 ] = None,
                 *,
                 format: str = 'DD-MM-YYYY',
                 valueFormat: str = 'DD-MM-YYYY',
                 on_change: Optional[Callable[..., Any]] = None) -> None:
        """Date Input

        :param value: the initial date
        :param mask: the format of the date string (default: 'YYYY-MM-DD')
        :param on_change: callback to execute when changing the date
        """
        super().__init__()
        self._props['value'] = value
        self._props['format'] = format
        self._props['valueFormat'] = valueFormat


        self.on('update:value', lambda e : on_change(e))

        
