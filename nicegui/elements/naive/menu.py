from typing import Any, Callable, Dict, List, Optional, Union
from ...element import Element
from .anchor import AnchorNve

class MenuNve(AnchorNve, component='menun.js'):

    def __init__(self,
                options: List[Dict] = [],
                on_click: Optional[Callable[..., Any]] = None) -> None:
        """
        """
        super().__init__(on_click=on_click)
        self._props['optionsValue'] = options

        #self.on('click', lambda e : on_click(e))
