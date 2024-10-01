from typing import Any, Callable, Dict, List, Optional, Union

from ..mixins.disableable_element import DisableableElement

class DateVfy(DisableableElement, component='datev.js'):

    def __init__(self,
                 value: Optional[
                     Union[str, Dict[str, str], List[str], List[Union[str, Dict[str, str]]]]
                 ] = None,
                 *,
                 mask: str = 'dd-MM-yyyy',
                 on_change: Optional[Callable[..., Any]] = None) -> None:
        """Date Input

        ui.dateVfy('30-04-2020', mask='dd-MM-yyyy', on_change=lambda e: ui.notify(e.args)) #  solo date


        :param value: the initial date
        :param mask: the format of the date string (default: 'YYYY-MM-DD')
        :param on_change: callback to execute when changing the date
        """
        super().__init__()
        self._props['value'] = value
        self._props['dateFormat'] = mask

        self.on('update:value', lambda e : on_change(e))

        
