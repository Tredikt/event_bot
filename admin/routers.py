from admin.handlers.command.admin import admin_command_router
from admin.handlers.callback.admin import admin_callback_router


admin_routers = [
    # COMMAND
    admin_command_router,
    # CALLBACK
    admin_callback_router,

    # # STATE
    # mailing_state_router,

]