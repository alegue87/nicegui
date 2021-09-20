class Ui:
    from .run import run, config  # NOTE: before justpy

    from .elements.button import Button as button
    from .elements.checkbox import Checkbox as checkbox
    from .elements.custom_example import CustomExample as custom_example
    from .elements.dialog import Dialog as dialog
    from .elements.icon import Icon as icon
    from .elements.image import Image as image
    from .elements.input import Input as input
    from .elements.joystick import Joystick as joystick
    from .elements.html import Html as html
    from .elements.label import Label as label
    from .elements.link import Link as link
    from .elements.log import Log as log
    from .elements.markdown import Markdown as markdown
    from .elements.menu import Menu as menu
    from .elements.menu_item import MenuItem as menu_item
    from .elements.notify import Notify as notify
    from .elements.number import Number as number
    from .elements.page import Page as page
    from .elements.radio import Radio as radio
    from .elements.scene import Scene as scene
    from .elements.select import Select as select
    from .elements.slider import Slider as slider
    from .elements.svg import Svg as svg
    from .elements.switch import Switch as switch
    from .elements.toggle import Toggle as toggle
    from .elements.upload import Upload as upload

    from .elements.plot import Plot as plot
    from .elements.line_plot import LinePlot as line_plot

    from .elements.row import Row as row
    from .elements.column import Column as column
    from .elements.card import Card as card
    from .elements.card import CardSection as card_section

    from .timer import Timer as timer

    from .lifecycle import startup_tasks, on_startup, shutdown_tasks, on_shutdown

    def __init__(self, app) -> None:
        self.app = app

    def get(self, path: str):
        """
        Use as a decorator for a function like @ui.get('/another/route/{id}').
        :param path: String that starts with a '/'.
        :return:
        """
        def decorator(func):
            from starlette.routing import Route
            self.add_route(Route(path, func))
            return func
        return decorator

    def add_route(self, route):
        """
        :param route: A starlette Route including a path and a function to be called.
        :return:
        """
        self.app.routes.insert(0, route)
