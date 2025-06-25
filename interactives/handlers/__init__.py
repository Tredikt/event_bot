from interactives.handlers.callback import callback_routers
from interactives.handlers.state import state_routers


interactive_routers = [
    *callback_routers,
    *state_routers
]