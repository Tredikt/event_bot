from interactives.handlers.callback.tests import router
from admin.routers import admin_routers


routers = [
    *admin_routers,
    router,
]
