from admin.handlers.callback import admin_callback_router
from admin.handlers.command import admin_command_router


admin_routers = [
    # COMMAND
    admin_command_router,
    # CALLBACK
    admin_callback_router,

    # # STATE
    # mailing_state_router,

]