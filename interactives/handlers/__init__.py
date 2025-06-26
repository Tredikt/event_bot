from interactives.handlers.callback import callback_routers
from interactives.handlers.state import state_routers
from interactives.handlers.command import start_command_router


interactive_routers = [
    *callback_routers,
    *state_routers,
    start_command_router
]