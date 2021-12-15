from trame.app import get_app_instance
from trame.dev import main
from trame.layouts import update_layout
from trame.server import port, start, stop
from trame.state import (
    change, flush_state, get_state, is_dirty, is_dirty_all, State, update_state
)
from trame.trigger import trigger, trigger_key
from trame.utils import (
    get_cli_parser, get_version, log_js_error, print_server_info,
    validate_key_names
)

__version__ = get_version()

state = State()
"""This object provides pythonic access to the state

For instance, these getters are the same:

>>> field, = get_state("field")
>>> field = state.field

As are these setters:

>>> update_state("field", value)
>>> state.field = value

``get_state()`` should be used instead if more than one argument is to be
passed, and ``update_state()`` should be used instead to specify additional
arguments (e.g. ``force=True``).

This object may be imported via

>>> from trame import state
"""

__all__ = [
    # Order these how we want them to show up in the docs
    "start",
    "stop",
    "port",
    "state",
    "update_state",
    "get_state",
    "update_layout",
    "get_cli_parser",
    "flush_state",
    "is_dirty",
    "is_dirty_all",
    "change",
    "trigger",

    # These are not exposed in the docs
    "__version__",
    "get_app_instance",
    "get_version",
    "log_js_error",
    "main",
    "print_server_info",
    "trigger_key",
    "validate_key_names",
]
