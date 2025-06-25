from interactives.handlers import interactive_routers
from admin.handlers import admin_routers


routers = [
    *admin_routers,
    *interactive_routers,
]