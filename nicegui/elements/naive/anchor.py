from typing import Any, Callable, Dict, List, Optional, Union
from ...element import Element

class AnchorNve(Element, component='anchorn.js'):

    def __init__(self,
                on_click: Optional[Callable[..., Any]] = None) -> None:
        """
        """
        super().__init__()

        self.on('click:value', lambda e : on_click(e))
