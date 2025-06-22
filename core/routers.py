from interactives.handlers.callback.tests import test_router
from admin.routers import admin_routers


routers = [
    *admin_routers,
    test_router,
]
