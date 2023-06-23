from pathlib import Path
from typing import Union

from nicegui.dependencies import register_vue_component

from .mixins.source_element import SourceElement

register_vue_component('image', Path(__file__).parent / 'image.js')


class Image(SourceElement):

    def __init__(self, source: Union[str, Path] = '') -> None:
        """Image

        Displays an image.

        :param source: the source of the image; can be a URL, local file path or a base64 string
        """
        super().__init__(tag='image', source=source)
        self.use_component('image')
