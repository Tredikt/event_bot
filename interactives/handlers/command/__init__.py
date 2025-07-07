from interactives.handlers.command.start import router as start_command_router
from interactives.handlers.command.support import router as support_command_router
from interactives.handlers.command.event import router as event_command_router
from interactives.handlers.command.order import router as order_command_router


commands_routers = [
    start_command_router,
    support_command_router,
    event_command_router,
    order_command_router,
]